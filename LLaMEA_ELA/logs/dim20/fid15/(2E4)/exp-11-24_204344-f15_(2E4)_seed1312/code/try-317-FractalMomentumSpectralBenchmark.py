import numpy as np

class FractalMomentumSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal dimensions and spectral weights
        self.fractal_dims = np.array([1.3 + 0.2 * np.sin(i * 0.6) for i in range(dim)])
        self.spectral_weights = np.array([0.5 + 0.5 * np.cos(i * 0.4) for i in range(dim)])
        # Evolutionary momentum parameters
        self.momentum_decay = 0.95 + 0.02 * np.sin(dim * 0.3)
        self.momentum_strength = 1.0 + 0.3 * np.cos(dim * 0.2)
        
    def f(self, x):
        x = np.array(x)
        
        # Fractal-based self-similarity term with scale-invariant ruggedness
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale Gaussian peaks with varying widths and heights
            scales = [0.5, 1.0, 2.0, 3.0]
            heights = [1.0, 2.5, 1.8, 3.2]
            positions = [-4.0, -2.0, 0.0, 2.0]
            
            for scale, height, pos in zip(scales, heights, positions):
                # Scale-invariant Gaussian with fractal dimension modulation
                sigma = scale * (1.0 + 0.2 * np.sin(x[i] * 0.5))
                fractal_term += height * np.exp(-0.5 * ((x[i] - pos) / sigma)**(2.0 * self.fractal_dims[i]))
        
        # Evolutionary momentum dynamics with memory effects
        momentum_term = 0.0
        for i in range(self.dim):
            # Simulate momentum decay and strength
            momentum = self.momentum_strength * np.sin(x[i] * 0.7) * np.exp(-self.momentum_decay * np.abs(x[i]))
            momentum_term += momentum**2
        
        # Spectral decomposition with frequency-domain interactions
        spectral_term = 0.0
        # Discrete Fourier Transform approach for spectral components
        fft_x = np.fft.fft(x)
        freqs = np.arange(len(fft_x))
        for k in range(len(fft_x)):
            # Weighted frequency components with phase modulation
            weight = self.spectral_weights[k % self.dim]
            phase = np.angle(fft_x[k]) * (1.0 + 0.1 * np.sin(freqs[k] * 0.3))
            spectral_term += weight * np.abs(fft_x[k])**2 * np.cos(phase)
        
        # Coupling between dimensions using a fractal-like interaction matrix
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling strength based on distance and dimensionality
                dist = np.abs(x[i] - x[j])
                coupling_strength = 0.3 * (1.0 + np.sin(dist * 0.5)) / (1.0 + dist**2)
                coupling_term += coupling_strength * (x[i]**2 + x[j]**2)
        
        # Adaptive conditioning with chaotic modulation
        conditioning_factor = 1.0 + 0.5 * np.sin(self.dim * 0.4) * np.cos(self.dim * 0.1)
        
        # Final combination of all terms
        total = 0.3 * fractal_term + 0.25 * momentum_term + 0.2 * spectral_term + \
                0.25 * coupling_term
        
        return total * conditioning_factor