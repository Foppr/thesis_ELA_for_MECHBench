import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic trigonometric components with adaptive frequencies
        trig_component = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.2 * x[i])
            trig_component += np.sin(freq * x[i]) * np.cos(0.3 * x[i]**2) * np.exp(-0.1 * abs(x[i]))
        
        # Adaptive radial basis functions with dynamic centers and widths
        rbf_component = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0.0
            width = 0.5 + 0.3 * np.cos(0.1 * x[i])
            rbf_component += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.sin(0.4 * x[i])
        
        # Gradient-based attraction-repulsion fields
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
            gradient_field += (grad_attraction - grad_repulsion) * np.tanh(x[i])
        
        # Cross-dimensional polynomial coupling with variable exponents
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_i = 2 + int(3 * np.sin(0.1 * x[i]))
                exp_j = 2 + int(3 * np.cos(0.1 * x[j]))
                poly_coupling += (x[i]**exp_i + x[j]**exp_j) * np.cos(0.2 * x[i] * x[j])
        
        # Nonlinear transformation with exponential decay
        nonlinear_transform = 0
        for i in range(self.dim):
            nonlinear_transform += np.exp(-0.5 * x[i]**2) * np.sin(2 * x[i]) * np.cos(0.5 * x[i])
        
        # Dimensionality-dependent scaling and weighting
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.3) + 0.1 * np.cos(self.dim * 0.1)
        
        # Combine all components with optimized weights
        return scale_factor * (0.3 * trig_component + 0.25 * rbf_component + 
                              0.2 * gradient_field + 0.15 * poly_coupling + 
                              0.1 * nonlinear_transform)