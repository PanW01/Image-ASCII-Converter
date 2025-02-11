using System;
using System.Text;
using System.Collections.Generic;
using System.Threading;

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
    }
}