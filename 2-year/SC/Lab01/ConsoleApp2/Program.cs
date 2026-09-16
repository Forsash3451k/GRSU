using System.Drawing;
using System.Drawing.Imaging;
using System.Text;
using System.Text.RegularExpressions;
using static System.Net.Mime.MediaTypeNames;

namespace ConsoleApp2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите путь к текстовому файлу: ");
            string? filePath = null;
            while (filePath == null)
                filePath = Console.ReadLine();

            string text = File.ReadAllText(filePath, Encoding.UTF8);
            List<Color> colors = new List<Color>();

            Dictionary<string, Color> ColorMap = new(StringComparer.OrdinalIgnoreCase)
            {
                { "красн", Color.Red },
                { "алый",  Color.Crimson },
                { "алая",  Color.Crimson },
                { "алого", Color.Crimson },
                { "алые",  Color.Crimson },
                { "багр", Color.DarkRed },
                { "зелен", Color.Green },
                { "изумруд", Color.MediumSeaGreen },
                { "малахит", Color.MediumSeaGreen },
                { "син", Color.Blue },
                { "голуб", Color.LightBlue },
                { "лазур", Color.LightSkyBlue },
                { "ультрамарин", Color.Blue },
                { "желт", Color.Yellow },
                { "золот", Color.Gold },
                { "лимон", Color.LemonChiffon },
                { "бел", Color.White },
                { "черн", Color.Black },
                { "сер", Color.Gray },
                { "фиолетов", Color.Purple },
                { "лилов", Color.Purple },
                { "оранжев", Color.Orange },
                { "коричнев", Color.Brown },
                { "розов", Color.Pink },
                { "бирюз", Color.Turquoise },
            };

            MatchCollection words = Regex.Matches(text, @"\b[\p{IsCyrillic}a-zA-Z]+\b");
            foreach (Match match in words)
            {
                string word = match.Value.ToLowerInvariant();
                foreach (var kvp in ColorMap)
                {
                    if (word.StartsWith(kvp.Key, StringComparison.OrdinalIgnoreCase))
                    {
                        colors.Add(kvp.Value);
                        break;
                    }
                }
            }

            if (colors.Count == 0)
            {
                Console.WriteLine("Во входном файле нету цветов");
                return;
            }


            Console.Write("Введите путь к выходному файлу: ");
            string? outPath = null;
            while (outPath == null)
                outPath = Console.ReadLine();
            GenerateImage(colors, outPath);
        }
        private static void GenerateImage(List<Color> colors, string outputPath)
        {
            const int squareSize = 20;
            const int padding = 2;
            const int columns = 20;

            int count = colors.Count;
            int rows = (int)Math.Ceiling((double)count / columns);

            int margin = 10;
            int totalWidth = columns * squareSize + (columns - 1) * padding + 2 * margin;
            int totalHeight = rows * squareSize + (rows - 1) * padding + 2 * margin;

            using var bitmap = new Bitmap(totalWidth, totalHeight);
            using var g = Graphics.FromImage(bitmap);
            g.Clear(Color.White);

            int x = margin, y = margin;
            for (int i = 0; i < count; i++)
            {
                using var brush = new SolidBrush(colors[i]);
                g.FillRectangle(brush, x, y, squareSize, squareSize);

                if ((i + 1) % columns == 0)
                {
                    x = margin;
                    y += squareSize + padding;
                }
                else
                {
                    x += squareSize + padding;
                }
            }

            bitmap.Save(outputPath, ImageFormat.Png);
        }
    }
}
