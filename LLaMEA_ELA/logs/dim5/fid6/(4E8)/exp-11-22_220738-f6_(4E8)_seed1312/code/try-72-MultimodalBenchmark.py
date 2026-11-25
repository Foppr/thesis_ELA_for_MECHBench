import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Highly modified chaotic parameters for increased complexity
        self.a = 4.02
        self.r = 0.67
        self.seed = 0.19
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with modified coefficient
        f_val = 0.8 * np.sum(x**2)
        
        # Enhanced chaotic modulation using a modified logistic map with multiple feedback loops
        chaos_factor = self.seed
        for i in range(self.dim):
            chaos_factor = self.a * chaos_factor * (1 - chaos_factor) + 0.1 * np.sin(chaos_factor * x[i])
            if i < len(x):
                f_val += 1.2 * np.sin(chaos_factor * x[i]) * np.cos(0.6 * x[i]) * np.sin(0.35 * x[i])
        
        # Dense Gaussian peaks with randomized positions, widths, and heights
        peak_centers = np.linspace(-4.8, 4.8, min(12, self.dim))
        for i in range(len(peak_centers)):
            if i < self.dim:
                center = peak_centers[i % len(peak_centers)]
                width = 0.2 + 0.7 * np.sin(i * 0.8 + x[i % len(x)])
                height = 0.3 + 0.7 * np.cos(i * 0.4 + x[(i+1) % len(x)])
                f_val += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Fractal-like oscillations with nested frequency modulation and phase shifts
        freq_mod = 1.2
        for i in range(self.dim):
            freq_mod = 1 + 0.3 * np.sin(freq_mod * x[i]) + 0.2 * np.cos(freq_mod * x[i]) + 0.15 * np.tan(0.5 * freq_mod)
            f_val += 0.45 * np.sin(freq_mod * x[i]) * np.cos(5.0 * x[i]) * np.tan(0.4 * x[i])
            
        # Enhanced saddle point structure with multi-directional dependency and higher-order non-linearity
        if self.dim >= 2:
            for i in range(self.dim - 1):
                f_val += 0.35 * (x[i]**4 - x[i+1]**4) * np.cos(0.9 * x[i]) + 0.2 * (x[i] - x[i+1])**3
                
        # Stronger cross-dimensional coupling with exponential interaction and trigonometric modulation
        if self.dim >= 3:
            for i in range(self.dim - 2):
                f_val += 0.35 * np.exp(-abs(x[i] + x[i+1] + x[i+2])) * np.sin(0.7 * x[i]) * np.cos(0.3 * x[i+1]) + 0.18 * np.sin(2.0 * x[i+2])
                
        # Additional high-frequency oscillatory component with chaotic amplitude modulation
        for i in range(self.dim):
            amp_mod = 1 + 0.25 * np.sin(x[i] * 0.5) * np.cos(x[i] * 0.3)
            f_val += amp_mod * 0.22 * np.sin(12.0 * x[i]) * np.cos(8.5 * x[i])
            
        return f_val