import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic tent map component with parameter dependence
        tent_map = 0.0
        for i in range(self.dim - 1):
            xi = x_norm[i]
            xi1 = x_norm[i + 1]
            # Tent map dynamics with chaotic behavior
            if xi < 0.5:
                tent_val = 2 * xi
            else:
                tent_val = 2 * (1 - xi)
            
            if xi1 < 0.5:
                tent_val1 = 2 * xi1
            else:
                tent_val1 = 2 * (1 - xi1)
            
            tent_map += tent_val * tent_val1
        
        # Radial basis function valleys with adaptive spread and amplitude
        rbf = 0.0
        for i in range(self.dim):
            # Dynamic spread based on dimension
            sigma = 0.5 + 0.2 * np.sin(i * np.pi / self.dim)
            # Adaptive amplitude
            amp = 1.0 + 0.3 * np.cos(i * np.pi / self.dim)
            rbf += amp * np.exp(-0.5 * (x_norm[i] / sigma)**2)
        
        # Gradient-based saddle structure with directional coupling
        saddle = 0.0
        for i in range(self.dim - 1):
            xi = x_norm[i]
            xi1 = x_norm[i + 1]
            # Directional gradient interaction
            grad_term = (xi**3 - xi) * (xi1**3 - xi1)
            saddle += grad_term
        
        # Cross-dimensional coupling with chaotic logistic map interactions
        logistic_coupling = 0.0
        r = 3.9  # Chaotic regime parameter
        for i in range(self.dim - 1):
            xi = x_norm[i]
            xi1 = x_norm[i + 1]
            logistic_val = r * xi * (1 - xi)
            logistic_val1 = r * xi1 * (1 - xi1)
            logistic_coupling += logistic_val * logistic_val1
        
        # High-frequency oscillatory component with exponential decay
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += np.sin(20 * x_norm[i]) * np.cos(15 * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
        
        # Dimension-dependent conditioning factor with chaotic growth
        condition_factor = 1.0 + 0.4 * np.sin(self.dim * np.pi / 4.0) + 0.1 * np.log(self.dim + 1)
        
        # Combine all terms
        return condition_factor * (tent_map + rbf + saddle + logistic_coupling + oscillatory)