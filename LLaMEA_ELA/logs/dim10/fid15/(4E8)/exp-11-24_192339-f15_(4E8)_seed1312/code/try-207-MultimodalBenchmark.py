import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Intensified chaotic modulation with sine-cosine mixing
        chaotic_component = 0
        for i in range(self.dim):
            freq1 = 2.0 + 1.5 * np.sin(0.3 * x[i])
            freq2 = 1.0 + 0.8 * np.cos(0.4 * x[i])
            chaotic_component += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.2 * abs(x[i]))
        
        # Dynamic radial basis functions with quaternion-inspired centers
        rbf_component = 0
        for i in range(self.dim):
            center_i = 3.0 * np.sin(0.5 * x[i])
            center_j = 3.0 * np.cos(0.5 * x[i])
            width = 1.0 + 0.5 * np.sin(0.2 * x[i])
            rbf_component += np.exp(-0.5 * ((x[i] - center_i) / width)**2) * np.exp(-0.5 * ((x[i] - center_j) / width)**2)
        
        # Gradient-based attraction-repulsion fields with anti-symmetric coupling
        gradient_field = 0
        for i in range(self.dim):
            grad_attraction = 0
            grad_repulsion = 0
            for j in range(self.dim):
                if i != j:
                    dist = abs(x[i] - x[j])
                    attraction = np.exp(-dist) * np.sin(dist)
                    repulsion = np.exp(-dist**2) * np.cos(dist)
                    grad_attraction += attraction
                    grad_repulsion += repulsion
            # Anti-symmetric coupling term
            gradient_field += (grad_attraction - grad_repulsion) * np.tanh(x[i]) * np.sign(x[i])
        
        # Enhanced polynomial couplings with fractal-like recursive structure
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_i = 3 + int(4 * np.sin(0.15 * x[i]))
                exp_j = 3 + int(4 * np.cos(0.15 * x[j]))
                poly_coupling += (x[i]**exp_i + x[j]**exp_j) * np.cos(0.3 * x[i] * x[j]) * np.sin(0.2 * (x[i] + x[j]))
        
        # Hyperbolic tangent-based cross-dimensional interactions
        tanh_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                tanh_interaction += np.tanh(x[i]) * np.tanh(x[j]) * np.sin(0.25 * x[i] * x[j])
        
        # Fractal-like recursive structure with anti-symmetric coupling
        fractal_component = 0
        for i in range(self.dim):
            fractal_component += np.sin(3 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Nonlinear transformation with exponential decay and periodic modulation
        nonlinear_transform = 0
        for i in range(self.dim):
            nonlinear_transform += np.exp(-0.3 * x[i]**2) * np.sin(3 * x[i]) * np.cos(0.7 * x[i]) * np.sin(0.1 * x[i])
        
        # Dimensionality-dependent scaling and weighting with recursive complexity
        scale_factor = 1.5 + 0.3 * np.sin(self.dim * 0.4) + 0.2 * np.cos(self.dim * 0.2) + 0.1 * np.sin(self.dim * 0.6)
        
        # Combine all components with optimized weights
        return scale_factor * (0.25 * chaotic_component + 0.2 * rbf_component + 
                              0.18 * gradient_field + 0.17 * poly_coupling + 
                              0.12 * tanh_interaction + 0.08 * fractal_component + 
                              0.08 * nonlinear_transform)