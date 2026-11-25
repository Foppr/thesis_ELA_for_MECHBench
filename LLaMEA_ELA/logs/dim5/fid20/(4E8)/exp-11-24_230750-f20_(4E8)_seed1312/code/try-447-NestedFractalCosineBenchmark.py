import numpy as np

class NestedFractalCosineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters
        self.fractal_centers = np.random.uniform(-4, 4, (dim, 3))
        self.fractal_scales = np.random.uniform(0.5, 2.0, (dim, 3))
        self.cosine_frequencies = np.random.uniform(1.0, 5.0, dim)
        self.adaptive_weights = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested fractal peak component with dynamic scaling
        fractal = 0.0
        for i in range(self.dim):
            peak_sum = 0.0
            for j in range(3):
                center = self.fractal_centers[i, j]
                scale = self.fractal_scales[i, j]
                # Fractal-like Gaussian with dynamic scaling
                peak_sum += np.exp(-0.5 * ((x[i] - center) / (scale * (1.0 + 0.1 * np.sin(0.3 * x[i]))))**2)
            fractal += peak_sum
        
        # Dynamic cosine modulation with adaptive frequencies
        cos_mod = 0.0
        for i in range(self.dim):
            freq = self.cosine_frequencies[i] * (1.0 + 0.2 * np.sin(0.4 * x[i]))
            cos_mod += np.cos(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive conditioning based on dimension
        cond_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Cross-dimensional coupling with nested structure
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Nested coupling with dynamic weights
                weight = self.adaptive_weights[i] * self.adaptive_weights[j]
                dist = np.abs(x[i] - x[j])
                coupling += weight * np.sin(0.5 * dist) * np.cos(0.3 * (x[i] + x[j]))
        
        # Hyperbolic tangent saddle point structure
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                tanh_term = np.tanh(0.5 * x[i] + 0.3 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * tanh_term
        
        # Memory-enhanced sine-wave component with nested modulations
        memory_sine = 0.0
        for i in range(self.dim):
            # Memory effect from previous dimension
            mem_factor = 1.0 + 0.1 * np.sin(0.2 * x[i-1]) if i > 0 else 1.0
            memory_sine += mem_factor * np.sin(2.0 * x[i] + 0.5 * np.cos(0.3 * x[i])) * np.exp(-0.05 * x[i]**2)
        
        # Fractal-like cosine component with multi-scale modulation
        fractal_cos = 0.0
        for i in range(self.dim):
            # Multi-scale cosine with fractal behavior
            scale_factor = 1.0 + 0.2 * np.sin(0.4 * x[i])
            freq_mod = 1.0 + 0.3 * np.cos(0.2 * x[i])
            fractal_cos += np.cos(freq_mod * x[i] * scale_factor) * np.exp(-0.1 * x[i]**2)
        
        # Combine all components with optimized weights
        return (0.25 * fractal + 0.20 * cos_mod + 0.15 * coupling + 
                0.15 * saddle + 0.12 * memory_sine + 0.13 * fractal_cos) * cond_factor