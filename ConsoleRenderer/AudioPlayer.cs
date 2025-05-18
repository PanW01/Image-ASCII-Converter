using NAudio.Wave;
using System.Threading;

namespace ConsoleRendererLib
{
    public class AudioPlayer
    {
        public void Play(string pathTemporalAudioFile)
        {
            using var waveStream = new WaveFileReader(pathTemporalAudioFile);

            using var waveOut = new WaveOutEvent();
            waveOut.Init(waveStream);
            waveOut.Play();

            while (waveOut.PlaybackState == PlaybackState.Playing)
            {
                Thread.Sleep(100);
            }
        }
    }
}