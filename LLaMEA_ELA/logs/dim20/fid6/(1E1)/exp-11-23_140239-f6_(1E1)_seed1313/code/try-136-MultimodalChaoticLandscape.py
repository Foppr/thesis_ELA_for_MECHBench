import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add exponentially decaying harmonic waves with adaptive frequencies
        for i in range(1, min(self.dim + 1, 20)):
            freq = 2 ** i
            amp = 10.0 / (1.0 + i * 0.5)
            result += amp * np.sin(freq * x[i-1]) * np.exp(-0.1 * abs(x[i-1]))
        
        # Add cross-dimensional coupling with chaotic modulation
        for i in range(self.dim - 1):
            coupling = np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+1])
            result += 2.0 * coupling * np.exp(-0.05 * (i + 1))
        
        # Add fractal-like multiscale component with varying amplitudes
        for i in range(1, min(self.dim + 1, 15)):
            scale = 3.0 / (1.0 + 0.2 * i)
            result += 5.0 * np.sin(scale * x[i-1]) * np.cos(scale * x[i-1] * 0.5) * np.exp(-0.02 * i**2)
        
        # Add chaotic noise component with dimensionality-dependent intensity
        noise_intensity = 1.0 + 0.5 * np.sin(self.dim * 0.8)
        noise = noise_intensity * np.sum(np.sin(50 * x) * np.cos(30 * x) * np.sin(10 * x))
        
        # Add adaptive basin splitting with exponential decay
        basin_split = 0.0
        for i in range(self.dim):
            basin_split += 3.0 * np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(10 * x[i])
        
        # Add multi-modal harmonic terms with varying phase shifts
        modal_term = 0.0
        for i in range(self.dim):
            phase_shift = i * 0.3
            modal_term += 4.0 * np.cos(8 * x[i] + phase_shift) * np.sin(6 * x[i] + phase_shift)
        
        return result + noise + basin_split + modal_term