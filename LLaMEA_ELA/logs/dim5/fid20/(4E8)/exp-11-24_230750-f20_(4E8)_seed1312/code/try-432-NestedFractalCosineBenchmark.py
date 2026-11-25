import numpy as np

class NestedFractalCosineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute nested fractal parameters
        self.fractal_depth = np.random.randint(2, 5, dim)
        self.cosine_amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.cosine_frequencies = np.random.uniform(0.5, 2.5, dim)
        self.peaks_centers = np.random.uniform(-4, 4, (dim, 3))
        self.peaks_heights = np.random.uniform(0.5, 2.0, (dim, 3))
        self.conditioning_factors = np.random.uniform(0.8, 1.5, dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested fractal peaks with dynamic cosine modulations
        nested_peaks = 0.0
        for i in range(self.dim):
            depth = self.fractal_depth[i]
            peak_val = 0.0
            for j in range(3):
                center = self.peaks_centers[i, j]
                height = self.peaks_heights[i, j]
                sigma = 0.5 + 0.5 * np.sin(0.3 * x[i])
                # Nested structure: each peak is modulated by higher frequency cosine
                nested_mod = np.cos(self.cosine_frequencies[i] * (x[i] - center))
                peak_val += height * np.exp(-0.5 * ((x[i] - center) / sigma)**2) * nested_mod
            nested_peaks += peak_val
        
        # Dynamic cosine couplings with adaptive frequencies
        cosine_coupling = 0.0
        for i in range(self.dim):
            amp = self.cosine_amplitudes[i]
            freq = self.cosine_frequencies[i]
            # Adaptive frequency based on position and neighbors
            adaptive_freq = freq * (1.0 + 0.2 * np.sin(0.5 * x[i]))
            for j in range(i+1, min(i+3, self.dim)):
                diff = x[i] - x[j]
                # Dynamic coupling with memory effects
                mem_factor = 1.0 + 0.1 * np.cos(0.2 * (x[i-1] if i > 0 else 0))
                cosine_coupling += amp * mem_factor * np.cos(adaptive_freq * diff) * np.sin(0.3 * (x[i] + x[j]))
        
        # Fractal modulation using nested Chebyshev polynomials
        fractal_mod = 0.0
        for i in range(self.dim):
            depth = self.fractal_depth[i]
            # Nested Chebyshev evaluation
            poly_val = 1.0
            for k in range(1, depth+1):
                poly_val += np.cos(k * x[i]) * (0.5 + 0.3 * np.sin(0.4 * x[i]))
            fractal_mod += np.sin(1.2 * x[i]) * poly_val
        
        # Adaptive conditioning with dimension-dependent factors
        cond_factor = np.mean(self.conditioning_factors)
        
        # Cross-dimensional hyperbolic coupling with chaotic modulation
        hyperbolic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic modulation using sine map
                sine_map_val = np.sin(3.2 * x[i] % np.pi)
                weight = 1.0 + 0.3 * np.cos(sine_map_val)
                hyperbolic_coupling += weight * (1.0 / (1.0 + np.exp(-(x[i] - x[j]))) - 0.5) * np.sin(0.4 * (x[i] + x[j]))
        
        # Deceptive gradient component with nested structure
        deceptive = 0.0
        for i in range(self.dim):
            # Nested deceptive valleys using cosine modulation
            deceptive += np.cos(3.0 * x[i]) * np.sin(0.5 * x[i]) * (1.0 + 0.2 * np.cos(2.0 * x[i]))
        
        # Combine all components with dynamic weighting
        return (0.20 * nested_peaks + 0.25 * cosine_coupling + 0.20 * fractal_mod + 
                0.20 * hyperbolic_coupling + 0.15 * deceptive) * cond_factor