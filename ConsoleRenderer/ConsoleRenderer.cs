using System.Text;

namespace ConsoleRendererLib
{
    public class ConsoleRenderer
    {
        public void DrawFrames(List<string> frames, int fps)
        {
            Console.Clear();
            foreach (var frame in frames)
            {
                StringBuilder sb = new StringBuilder();
                sb.Append(frame);
                
                Console.SetCursorPosition(0, 0);
                Console.Write(sb.ToString());
                Thread.Sleep(1000 / fps);
            }
            Console.Clear();
        }

        public void DrawSingleImage(string frame)
        {
            Console.Clear();
            StringBuilder sb = new StringBuilder();
            sb.Append(frame);

            Console.SetCursorPosition(0, 0);
            Console.Write(sb.ToString());
        }
    }
}