import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.harmonic_freqs = [2.0 + 1.5 * np.sin(0.3 * i) for i in range(dim)]
        self.gaussian_centers = [-4.0 + 8.0 * np.random.random() for _ in range(dim)]
        self.gaussian_widths = [0.5 + 1.0 * np.cos(0.4 * i) for i in range(dim)]
        self.coupling_strengths = [0.3 + 0.4 * np.sin(0.5 * i) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add chaotic harmonic oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            freq = self.harmonic_freqs[i]
            amp = 1.0 + 0.5 * np.cos(0.6 * i)
            phase = 0.2 * np.sin(0.7 * i)
            result += amp * np.sin(freq * xi + phase) * np.exp(-0.1 * xi**2)
            
        # Add adaptive Gaussian peaks with dynamic centers and widths
        for i in range(self.dim):
            xi = x[i]
            center = self.gaussian_centers[i]
            width = self.gaussian_widths[i]
            height = 1.5 + 0.8 * np.sin(0.4 * i)
            result += height * np.exp(-0.5 * ((xi - center) / width)**2)
            
        # Add cross-dimensional coupling with chaotic interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = self.coupling_strengths[i] * self.coupling_strengths[j]
                interaction = np.sin(0.8 * x[i] + 0.6 * x[j]) * np.cos(0.5 * x[i] - 0.3 * x[j])
                result += coupling * interaction
                
        # Add time-varying chaotic modulation with exponential decay
        time_factor = np.exp(-0.02 * self.dim)
        for i in range(self.dim):
            xi = x[i]
            mod_amp = 0.8 * time_factor * np.sin(15.0 * xi + 0.5 * i)
            result += mod_amp * np.cos(10.0 * xi) * np.sin(7.0 * xi)
            
        # Add multi-scale chaotic ridge structures
        for i in range(self.dim):
            xi = x[i]
            # Multiple nested ridges with different characteristics
            result += 0.7 * np.exp(-0.5 * ((xi - 2.0) / 0.4)**2) * np.sin(4.0 * xi)
            result += 0.5 * np.exp(-0.5 * ((xi + 1.0) / 0.6)**2) * np.cos(3.0 * xi)
            result += 0.3 * np.exp(-0.5 * ((xi - 3.5) / 0.8)**2) * np.sin(2.0 * xi)
            
        # Add dynamic coupling between even-odd dimension pairs
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                strength = 0.6 * np.cos(0.5 * (i + 1))
                result += strength * np.sin(x[i] * x[i+1]) * np.exp(-0.1 * (x[i] - x[i+1])**2)
                
        # Add global scaling factor with chaotic modulation
        global_scale = 1.2 + 0.3 * np.sin(0.8 * self.dim)
        result *= global_scale
        
        return result