import numpy as np

class FractalInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal dimensionality control parameters
        self.fractal_dim = 1.5 + 0.5 * np.sin(dim)
        self.conditioning_factor = 2.0 + 0.3 * np.cos(dim)
        self.interference_strength = 1.8 + 0.4 * np.sin(dim)
        self.modulation_freq = 3.0 + 0.5 * np.cos(dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like harmonic component with dynamic frequency modulation
        fractal_sum = 0
        for i in range(self.dim):
            freq = self.modulation_freq * (1 + 0.3 * np.sin(i * self.fractal_dim))
            fractal_sum += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Multi-modal Gaussian components with dynamic positioning and scaling
        modal_sum = 0
        num_peaks = max(3, int(self.dim / 2))
        for k in range(num_peaks):
            peak_pos = np.array([5.0 * np.sin(k * np.pi / (num_peaks + 1)) for _ in range(self.dim)])
            peak_height = 1.0 + 0.5 * np.cos(k)
            sigma = 0.5 + 0.2 * np.sin(k)
            gaussian_term = np.exp(-np.sum(((x - peak_pos) / sigma) ** 2) / 2)
            modal_sum += peak_height * gaussian_term
            
        # Inter-dimensional interference patterns with dynamic coupling
        interference_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(self.interference_strength * (x[i] - x[j])) * np.cos(self.interference_strength * (x[i] + x[j]))
                interference_sum += coupling ** 2
                
        # Dynamic conditioning based on dimensionality
        condition_factor = self.conditioning_factor * (1 + 0.2 * np.sin(np.log(self.dim + 1)))
        
        # Asymmetric penalty for out-of-bounds regions
        penalty = 0
        for i in range(self.dim):
            if x[i] < -4.5 or x[i] > 4.5:
                penalty += 10.0 * (abs(x[i]) - 4.5) ** 2
                
        # Combined fitness with chaotic scaling
        result = condition_factor * (fractal_sum + modal_sum + interference_sum) + penalty
        
        # Add small random perturbation for robustness
        noise = 0.01 * np.random.normal(0, 1)
        
        return result + noise + 0.3 * self.dim