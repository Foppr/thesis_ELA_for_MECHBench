import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic tent map with dynamic parameter modulation
        tent_map = 0.0
        for i in range(self.dim):
            param = 1.7 + 0.3 * np.sin(i * 0.4 + np.pi/4)
            if x[i] < 0.5:
                tent_map += param * x[i]
            else:
                tent_map += param * (1 - x[i])
        
        # Modified radial basis functions with adaptive centers and variable widths
        rbf_sum = 0.0
        for i in range(min(7, self.dim)):
            center = 2.5 * np.sin(i * 0.6) + 1.5 * np.cos(i * 0.8)
            width = 0.6 + 0.3 * np.sin(i * 0.5 + np.pi/3)
            rbf_sum += np.exp(-0.5 * ((x[i] - center) / width)**2) * (1.0 + 0.1 * np.sin(i * 0.7))
        
        # Polynomial coupling with mixed degrees and adaptive weights
        poly_coupling = 0.0
        for i in range(self.dim - 3):
            weight = 0.8 + 0.2 * np.cos(i * 0.3)
            poly_coupling += weight * x[i]**2 * x[i+1]**3 * x[i+2]**2 * x[i+3]**4
        
        # Adaptive noise with dynamic frequency and amplitude
        noise = 0.03 * np.random.rand() * np.sum(np.sin(2.5 * x) * np.cos(1.2 * x) * (1.0 + 0.2 * np.sin(self.dim * 0.5)))
        
        # Dynamic conditioning with multi-scale factors
        condition_factor = 1.0 + 0.15 * np.sin(self.dim * 0.3) * np.mean(np.abs(x)) + \
                          0.25 * np.cos(self.dim * 0.4) * np.std(x)**2 + \
                          0.1 * np.sin(self.dim * 0.7) * np.max(np.abs(x)) + \
                          0.05 * np.cos(self.dim * 0.2) * np.mean(x**2)
        
        # Quadratic base with enhanced coupling and dynamic scaling
        quadratic = condition_factor * (np.sum(x**2) + 0.15 * np.sum(x**4) + 0.05 * np.sum(np.abs(x)**3))
        
        # Hyperbolic sine coupling term with directional weighting
        sinh_coupling = 0.6 * np.sum(np.sinh(0.4 * x[:-2]) * np.cosh(0.2 * x[2:]) * np.cos(0.1 * x[:-2]))
        
        # Novel cross-dimensional interaction term
        cross_term = 0.3 * np.sum((x[:-1] - x[1:])**2 * np.sin(x[:-1] + x[1:]))
        
        # Final combined function value
        return quadratic + tent_map + rbf_sum + poly_coupling + sinh_coupling + cross_term + noise