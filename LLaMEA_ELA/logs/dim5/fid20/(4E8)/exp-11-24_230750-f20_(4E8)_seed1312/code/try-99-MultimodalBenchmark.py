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
            param = 1.5 + 0.5 * np.sin(i * 0.3)
            if x[i] < 0.5:
                tent_map += param * x[i]
            else:
                tent_map += param * (1 - x[i])
        
        # Radial basis functions with dynamic centers and widths
        rbf_sum = 0.0
        for i in range(min(5, self.dim)):
            center = 3.0 * np.sin(i * 0.5) + 2.0 * np.cos(i * 0.7)
            width = 0.8 + 0.4 * np.sin(i * 0.6)
            rbf_sum += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Polynomial coupling with alternating signs and mixed degrees
        poly_coupling = 0.0
        for i in range(self.dim - 2):
            poly_coupling += (-1)**i * x[i]**3 * x[i+1]**2 * x[i+2]**4
        
        # Adaptive noise component with frequency modulation
        noise = 0.05 * np.random.rand() * np.sum(np.sin(3.0 * x) * np.cos(1.5 * x))
        
        # Dynamic conditioning based on dimension and variable values
        condition_factor = 1.0 + 0.2 * np.sin(self.dim * 0.4) * np.mean(np.abs(x)) + \
                          0.3 * np.cos(self.dim * 0.3) * np.std(x)**2 + \
                          0.1 * np.sin(self.dim * 0.6) * np.max(np.abs(x))
        
        # Quadratic base with dynamic scaling and coupling
        quadratic = condition_factor * np.sum(x**2 + 0.1 * x**4)
        
        # Hyperbolic sine coupling term with cross-dimensional interactions
        sinh_coupling = 0.5 * np.sum(np.sinh(0.5 * x[:-1]) * np.cosh(0.3 * x[1:]))
        
        # Final combined function value
        return quadratic + tent_map + rbf_sum + poly_coupling + sinh_coupling + noise