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
            a = 4.0 * (1 + 0.3 * np.sin(0.6 * i))
            if x[i] < 0.5:
                tent_val = a * x[i]
            else:
                tent_val = a * (1 - x[i])
            tent += 0.4 * tent_val * np.sin(23 * x[i]) ** 2
        
        # Dynamic Gaussian radial basis functions with time-varying widths
        gaussian = 0
        for i in range(self.dim):
            center = 4.5 * np.sin(0.4 * i)
            width = 0.6 + 0.4 * np.cos(0.5 * i)
            gaussian += 0.5 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Asymmetric polynomial cross-dimensional interactions
        poly_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asym_factor = 1.0 + 0.4 * np.sin(0.8 * (i - j))
                if i < j:
                    poly_cross += asym_factor * x[i]**3 * x[j]**2
                else:
                    poly_cross += asym_factor * x[i]**2 * x[j]**3
        
        # Hyperbolic tangent-based coupling with dynamic scaling
        tanh_coupling = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                scale = 1.0 + 0.6 * np.sin(i)
                tanh_coupling += scale * np.tanh(x[i]) * np.tanh(x[i+1]) * (x[i]**2 + x[i+1]**2)
        
        # Quaternion-inspired interactions
        quat = 0
        for i in range(0, self.dim, 4):
            if i + 3 < self.dim:
                quat += 0.3 * (x[i]**2 + x[i+1]**2) * (x[i+2]**2 + x[i+3]**2) * np.sin(x[i] * x[i+1])
        
        # Logarithmic conditioning with exponential dimensionality dependence
        cond_factor = 1.0 + 1.0 * np.log(self.dim + 1) + 0.3 * np.exp(0.15 * self.dim)
        
        # Fractal-like self-similar structure with recursive polynomial terms
        fractal = 0
        for i in range(self.dim):
            fractal += 0.3 * (x[i]**6 + x[i]**5 + x[i]**4 + x[i]**3 + x[i]**2) * np.sin(13 * x[i])
        
        # Additional noise-like component with sinusoidal modulation
        noise = 0
        for i in range(self.dim):
            noise += 0.15 * np.sin(31 * x[i]) * np.cos(17 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Anti-symmetric coupling terms for increased complexity
        anti_sym = 0
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                anti_sym += 0.2 * (x[i] * x[i+1]**2 - x[i+1] * x[i+2]**2) * np.cos(7 * x[i])
        
        # Enhanced fractal component with multi-scale recursive structure
        enhanced_fractal = 0
        for i in range(self.dim):
            enhanced_fractal += 0.4 * (x[i]**7 + x[i]**6 + x[i]**5 + x[i]**4 + x[i]**3 + x[i]**2) * np.cos(11 * x[i])
        
        # Modified cross-dimensional coupling with increased nonlinearity
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += 0.15 * (x[i]**4 + x[j]**4) * np.sin(5 * (x[i] - x[j]))
        
        # Combine all components with appropriate weights and scaling
        return sphere + cond_factor * (0.35 * tent + 0.3 * gaussian + 0.25 * poly_cross + 0.2 * tanh_coupling + 0.15 * quat) + fractal + noise + anti_sym + enhanced_fractal + cross_coupling