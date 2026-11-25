import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Enhanced polynomial basin with fractional powers and variable coefficients
        basin_term = 0
        powers = [2.5, 3.7, 5.2, 6.8]
        coeffs = [0.35, 0.42, 0.28, 0.31]
        for i, (p, c) in enumerate(zip(powers, coeffs)):
            if i < len(x_norm):
                basin_term += c * np.abs(x_norm[i])**p
        
        # Fractal-like chaotic sinusoidal component with nested frequencies and phase shifts
        chaotic_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity
                freq1 = 25 + 5 * np.sin(0.5 * i)
                freq2 = 20 + 3 * np.cos(0.7 * j)
                chaotic_term += (np.sin(freq1 * x_norm[i]) * np.cos(freq2 * x_norm[j]) * 
                               np.exp(-0.1 * (x_norm[i] - x_norm[j])**2) +
                               np.cos(freq1 * x_norm[i]) * np.sin(freq2 * x_norm[j]) * 
                               np.exp(-0.05 * (x_norm[i] + x_norm[j])**2))
        
        # Multi-scale multimodal component with varying amplitude and frequency
        multimodal_term = 0
        for i in range(self.dim):
            # Multiple frequency components with different amplitudes
            freqs = [35, 45, 60]
            amps = [1.2, 0.8, 1.5]
            for f, a in zip(freqs, amps):
                multimodal_term += a * np.sin(f * x_norm[i]) * np.cos(f * x_norm[i]**2) + \
                                 a * np.cos(f * x_norm[i]**3) * np.sin(f * x_norm[i])
        
        # Novel coupling term with exponential decay and cross-dimension interaction
        coupling_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling_term += (np.sin(20 * x_norm[i]) * np.cos(15 * x_norm[j]) * 
                                np.exp(-dist**2) + 
                                np.cos(18 * x_norm[i]) * np.sin(12 * x_norm[j]) * 
                                np.exp(-dist**3))
        
        # Add a small fractal-like perturbation term
        fractal_perturbation = 0
        for i in range(self.dim):
            fractal_perturbation += np.sin(50 * np.sin(10 * x_norm[i])) * np.cos(40 * np.cos(8 * x_norm[i]))
        
        # Add a highly non-linear transformation with multiple chaotic maps
        chaotic_map = 0
        for i in range(self.dim):
            chaotic_map += np.sin(30 * np.sin(25 * np.sin(15 * x_norm[i]))) * \
                          np.cos(20 * np.cos(18 * np.cos(12 * x_norm[i])))
        
        # Combine all terms with adjusted weights
        result = 0.5 * basin_term + 0.7 * chaotic_term + 0.6 * multimodal_term + \
                0.4 * coupling_term + 0.3 * fractal_perturbation + 0.8 * chaotic_map
        
        # Add structured noise based on position and dimensionality
        noise = np.random.normal(0, 0.001 * (1 + 0.1 * self.dim))
        
        return result + noise