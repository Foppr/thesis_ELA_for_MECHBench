import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with parameter modulation
        tent_map = 0.0
        for i in range(self.dim):
            param = 1.7 + 0.3 * np.sin(i * 0.4)
            if x[i] < 0.5:
                tent_map += param * x[i]
            else:
                tent_map += param * (1 - x[i])
        
        # Radial basis functions with dynamic centers and widths
        rbf_sum = 0.0
        for i in range(min(5, self.dim)):
            center = 2.5 * np.sin(i * 0.6) + 1.5 * np.cos(i * 0.8)
            width = 0.9 + 0.3 * np.sin(i * 0.7)
            rbf_sum += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Polynomial coupling with alternating signs and mixed degrees
        poly_coupling = 0.0
        for i in range(self.dim - 2):
            poly_coupling += (-1)**(i+1) * x[i]**4 * x[i+1]**3 * x[i+2]**2
        
        # Adaptive noise component with frequency modulation
        noise = 0.03 * np.random.rand() * np.sum(np.sin(2.5 * x) * np.cos(1.2 * x))
        
        # Dynamic conditioning based on dimension and variable values
        condition_factor = 1.0 + 0.15 * np.sin(self.dim * 0.5) * np.mean(np.abs(x)) + \
                          0.25 * np.cos(self.dim * 0.4) * np.std(x)**2 + \
                          0.12 * np.sin(self.dim * 0.7) * np.max(np.abs(x))
        
        # Quadratic base with dynamic scaling and coupling
        quadratic = condition_factor * np.sum(x**2 + 0.08 * x**4)
        
        # Hyperbolic tangent coupling term with cross-dimensional interactions
        tanh_coupling = 0.6 * np.sum(np.tanh(0.4 * x[:-1]) * np.cosh(0.2 * x[1:]))
        
        # Final combined function value
        return quadratic + tent_map + rbf_sum + poly_coupling + tanh_coupling + noise