import numpy as np

class PolynomialRBFMixtureLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and widths for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Polynomial chaos expansion components with mixed degrees
        for i in range(self.dim):
            # Add different polynomial terms with varying coefficients
            result += 0.3 * x[i]**4 + 0.2 * x[i]**3 - 0.1 * x[i]**2 + 0.05 * x[i]
        
        # Radial basis function interactions
        rbf_sum = 0.0
        for j in range(10):
            center = self.centers[j]
            width = self.widths[j]
            distance = np.sum((x - center)**2)
            rbf_sum += np.exp(-distance / (2 * width**2))
        
        result += 0.5 * rbf_sum
        
        # Dynamic conditioning based on local feature density
        conditioning = 1.0
        for i in range(self.dim):
            # Local gradient approximation for conditioning
            grad_approx = np.abs(4 * 0.3 * x[i]**3 + 3 * 0.2 * x[i]**2 - 2 * 0.1 * x[i] + 0.05)
            conditioning += 0.1 * grad_approx
        
        # Add coupling between dimensions through a modified cosine interaction
        coupling_term = 0.0
        for i in range(self.dim - 1):
            coupling_term += np.cos(2 * (x[i] - x[i+1])) * (1 + 0.1 * np.sin(3 * x[i]))
        
        result += 0.2 * coupling_term
        
        # Multi-scale oscillatory behavior with varying frequencies
        oscillation = 0.0
        for i in range(self.dim):
            freq = 5 + i * 0.5
            oscillation += np.sin(freq * x[i]) * np.cos(2 * freq * x[i])
        
        result += 0.15 * oscillation
        
        # Add noise-dependent conditioning factor
        noise_factor = 1.0 + 0.05 * np.random.rand()
        
        # Apply final conditioning
        result *= conditioning * noise_factor
        
        # Asymmetric basin structure with modified symmetry breaking
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i]**5) * np.sin(0.3 * x[i]) + 0.2 * (x[i]**4) * np.cos(0.2 * x[i])
        
        result += 0.3 * asymmetry
        
        # Multi-modal peak structure with varying heights and widths
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += (
                0.8 * np.exp(-0.5 * (x[i] - 1.5)**2) * np.sin(4 * x[i]) +
                0.6 * np.exp(-0.5 * (x[i] + 1.5)**2) * np.cos(3 * x[i]) +
                0.4 * np.exp(-0.5 * x[i]**2) * np.sin(2 * x[i])
            )
        
        result += 0.2 * multimodal
        
        # Add regularization term
        result += 0.01 * np.sum(x**6)
        
        return result