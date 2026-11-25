import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic dynamical system component with hyperchaos and time-delayed feedback
        chaotic = 0.0
        for i in range(self.dim):
            # Hyperchaotic sine-cosine with delayed feedback and parameter modulation
            freq1 = 4.2 + 1.8 * np.sin(x_scaled[i] * 5.3)
            freq2 = 3.7 + 1.2 * np.cos(x_scaled[i] * 4.1)
            amp1 = 2.1 + 0.9 * np.sin(x_scaled[(i+1) % self.dim] * 2.7)
            amp2 = 1.8 + 0.6 * np.cos(x_scaled[(i-1) % self.dim] * 3.4)
            
            chaotic += amp1 * np.sin(freq1 * x_scaled[i]) * np.cos(freq2 * x_scaled[i]) + \
                      amp2 * np.sin(freq1 * x_scaled[i] * 0.6) * np.cos(freq2 * x_scaled[i] * 0.8)
        
        # Deep neural network-inspired interaction with multiple layers and activation
        nn_interaction = 0.0
        for i in range(self.dim):
            layer1 = 0.0
            for j in range(min(5, self.dim)):
                weight = 2.0 * np.sin(i * 0.7 + j * 0.5) * np.cos(i * 0.3 + j * 0.9)
                layer1 += weight * np.tanh(x_scaled[i] + x_scaled[(i+j) % self.dim])
            
            # Multi-layer activation with non-monotonic behavior
            nn_interaction += np.sin(layer1 * 2.5) * np.exp(-np.abs(layer1)) + \
                             np.cos(layer1 * 1.8) * np.log(1.0 + np.abs(layer1))
        
        # Extreme sharpness regions with multi-scale sigmoidal boundaries and fractal transitions
        sharpness = 0.0
        for i in range(self.dim):
            # Multiple extremely sharp transitions at different scales
            sharpness += (1.0 / (1.0 + np.exp(-50.0 * (x_scaled[i] - 0.3))) - 0.5)**2 + \
                        (1.0 / (1.0 + np.exp(-50.0 * (x_scaled[i] + 0.3))) - 0.5)**2 + \
                        (1.0 / (1.0 + np.exp(-45.0 * x_scaled[i])) - 0.5)**2 + \
                        (1.0 / (1.0 + np.exp(-60.0 * (x_scaled[i] - 0.6))) - 0.5)**2
        
        # Fractal wavelet component with self-similarity and multi-scale oscillation
        fractal_wave = 0.0
        scales = [1, 2, 3, 4, 6, 8]
        for scale in scales:
            for i in range(self.dim):
                # Wavelet-like structure with varying frequencies and amplitudes
                freq = scale * (2.0 + 0.5 * np.sin(i * 0.8))
                amp = 1.5 + 0.8 * np.cos(i * 0.6)
                fractal_wave += amp * np.sin(freq * x_scaled[i]) * \
                               np.cos(freq * x_scaled[i] * 0.7) * \
                               np.exp(-scale * np.abs(x_scaled[i]))
        
        # Multi-modal landscape with overlapping peaks and valleys
        multimodal = 0.0
        for i in range(self.dim):
            # Multiple local minima with varying depths and positions
            peak1 = 2.0 * np.exp(-((x_scaled[i] - 0.4)**2 + (x_scaled[(i+1) % self.dim] - 0.3)**2) / 0.1)
            peak2 = 1.5 * np.exp(-((x_scaled[i] + 0.5)**2 + (x_scaled[(i+1) % self.dim] + 0.4)**2) / 0.15)
            valley = 0.8 * np.exp(-((x_scaled[i] - 0.2)**2 + (x_scaled[(i+1) % self.dim] + 0.6)**2) / 0.2)
            multimodal += peak1 + peak2 + valley
        
        # Combined function with aggressive weighting for maximum algorithm discrimination
        return 1.5 * chaotic + 2.0 * nn_interaction + 3.0 * sharpness + 1.8 * fractal_wave + 2.5 * multimodal