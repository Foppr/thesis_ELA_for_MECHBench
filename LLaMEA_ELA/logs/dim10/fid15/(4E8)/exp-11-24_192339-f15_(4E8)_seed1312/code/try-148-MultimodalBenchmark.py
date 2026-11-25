import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Chaotic tent map multimodal component with dynamic parameter modulation
        tent = 0
        for i in range(self.dim):
            a = 3.8 * (1 + 0.2 * np.sin(0.5 * i))
            if x[i] < 0.5:
                tent_val = a * x[i]
            else:
                tent_val = a * (1 - x[i])
            tent += 0.3 * tent_val * np.sin(17 * x[i]) ** 2
        
        # Dynamic Gaussian radial basis functions with time-varying widths
        gaussian = 0
        for i in range(self.dim):
            center = 5.0 * np.sin(0.3 * i)
            width = 0.5 + 0.3 * np.cos(0.4 * i)
            gaussian += 0.4 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Asymmetric polynomial cross-dimensional interactions
        poly_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asym_factor = 1.0 + 0.3 * np.sin(0.7 * (i - j))
                if i < j:
                    poly_cross += asym_factor * x[i]**3 * x[j]**2
                else:
                    poly_cross += asym_factor * x[i]**2 * x[j]**3
        
        # Hyperbolic tangent-based coupling with dynamic scaling
        tanh_coupling = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                scale = 1.0 + 0.5 * np.sin(i)
                tanh_coupling += scale * np.tanh(x[i]) * np.tanh(x[i+1]) * (x[i]**2 + x[i+1]**2)
        
        # Logarithmic conditioning with exponential dimensionality dependence
        cond_factor = 1.0 + 0.8 * np.log(self.dim + 1) + 0.2 * np.exp(0.1 * self.dim)
        
        # Fractal-like self-similar structure with recursive polynomial terms
        fractal = 0
        for i in range(self.dim):
            fractal += 0.25 * (x[i]**5 + x[i]**4 + x[i]**3 + x[i]**2) * np.sin(11 * x[i])
        
        # Additional noise-like component with sinusoidal modulation
        noise = 0
        for i in range(self.dim):
            noise += 0.1 * np.sin(29 * x[i]) * np.cos(13 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Combine all components with appropriate weights and scaling
        return sphere + cond_factor * (0.3 * tent + 0.25 * gaussian + 0.2 * poly_cross + 0.15 * tanh_coupling) + fractal + noise