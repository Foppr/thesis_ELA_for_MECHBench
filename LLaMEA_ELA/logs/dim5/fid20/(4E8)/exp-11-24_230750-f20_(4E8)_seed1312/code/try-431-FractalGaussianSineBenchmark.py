import numpy as np

class FractalGaussianSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for logistic map
        self.logistic_r = np.random.uniform(3.57, 4.0, dim)
        self.gaussian_centers = np.random.uniform(-2.0, 2.0, dim)
        self.gaussian_widths = np.random.uniform(0.3, 1.5, dim)
        # Fractal dimension parameters
        self.fractal_dims = np.random.uniform(1.1, 1.9, dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like Gaussian peaks with memory effect
        fractal = 0.0
        prev_x = np.zeros(self.dim)
        for i in range(self.dim):
            center = self.gaussian_centers[i]
            sigma = self.gaussian_widths[i]
            # Fractal dimension scaling
            dim_scale = self.fractal_dims[i]
            # Memory effect from previous dimensions
            mem_factor = 1.0 + 0.2 * np.sin(0.5 * prev_x[i-1]) if i > 0 else 1.0
            fractal += mem_factor * np.exp(-0.5 * ((x[i] - center) / (sigma * dim_scale))**2)
            prev_x[i] = x[i]
        
        # Chaotic sine-wave couplings with tent map dynamics
        chaotic_sine = 0.0
        for i in range(self.dim):
            # Logistic map chaotic component
            logistic_val = self.logistic_r[i] * x[i] * (1 - x[i])
            # Sine-wave coupling with position-dependent frequency
            freq = 2.0 + 1.5 * np.sin(0.3 * x[i])
            chaotic_sine += np.sin(freq * logistic_val) * np.cos(0.4 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Memory-enhanced sine-wave couplings with adaptive weights
        memory_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Adaptive weight based on position and dimension
                weight = 1.0 + 0.2 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[j])
                # Memory effect from previous dimensions
                mem_i = 1.0 + 0.1 * np.sin(0.4 * prev_x[i-1]) if i > 0 else 1.0
                mem_j = 1.0 + 0.1 * np.sin(0.4 * prev_x[j-1]) if j > 0 else 1.0
                memory_coupling += weight * mem_i * mem_j * np.sin(x[i] - x[j]) * np.cos(0.3 * (x[i] + x[j]))
        
        # Adaptive conditioning with dimensionally varying parameters
        cond_factor = 1.0 + 0.25 * np.log(self.dim + 1)
        
        # Combine components with fractal scaling and enhanced nonlinearity
        return (0.35 * fractal + 0.30 * chaotic_sine + 0.35 * memory_coupling) * cond_factor