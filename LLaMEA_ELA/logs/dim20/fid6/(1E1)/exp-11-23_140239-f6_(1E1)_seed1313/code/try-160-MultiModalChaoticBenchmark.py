import numpy as np

class MultiModalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.05 * np.sum(x**2)
        
        # Add exponentially decaying sinusoidal waves with varying frequencies and amplitudes
        for i in range(1, min(self.dim + 1, 25)):
            freq = 2 ** i
            amp = 10.0 / (1.0 + i * 0.3)
            phase = np.pi * i * 0.7
            
            # Create wave pattern with adaptive curvature
            wave = amp * np.sin(freq * x[i-1] + phase) * np.exp(-0.1 * abs(x[i-1]))
            
            # Add local minima with varying depths
            depth = 2.0 / (1.0 + 0.5 * i)
            local_min = depth * np.cos(freq * x[i-1] + phase)
            
            result += wave + local_min
        
        # Add multi-modal noise component with adaptive frequency
        noise = 2.0 * np.sum(np.sin(30 * x) * np.cos(20 * x) * np.sin(10 * x))
        
        # Add chaotic coupling between dimensions with exponential decay
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += 5.0 * np.exp(-0.5 * (x[i] - x[i+1])**2) * np.sin(15 * (x[i] + x[i+1]))
        
        # Add fractal-like multiscale harmonics
        fractal = 0.0
        for i in range(1, min(self.dim + 1, 20)):
            scale = 2 ** (-i)
            fractal += scale * np.sin(20 * x[i-1] * scale) * np.cos(15 * x[i-1] * scale)
        
        # Add dimensionality-dependent modulation factor
        dim_mod = 1.0 + 0.8 * np.sin(self.dim * 0.5)
        
        # Add adaptive basin splitting
        basin_split = 0.5 * np.sum(np.sin(4 * x) * np.cos(3 * x) * np.tanh(x))
        
        return (result * dim_mod + noise + coupling + fractal + basin_split)