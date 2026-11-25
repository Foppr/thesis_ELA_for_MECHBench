import numpy as np

class RotatedMultiModalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrix for asymmetric effects
        self.rotation_matrix = np.random.rand(dim, dim) - 0.5
        self.rotation_matrix = np.dot(self.rotation_matrix, self.rotation_matrix.T)
        np.fill_diagonal(self.rotation_matrix, 1.0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to create asymmetric landscape
        x_rotated = np.dot(self.rotation_matrix, x)
        
        # Base polynomial component with global minimum at origin
        result = 0.1 * np.sum(x**2)
        
        # Add multiple polynomial terms with different exponents and coefficients
        for i in range(self.dim):
            result += 0.5 * (x_rotated[i]**6) + 0.3 * (x_rotated[i]**4) + 0.2 * (x_rotated[i]**2)
            
        # Add trigonometric components with varying frequencies and phases
        for i in range(self.dim):
            result += 0.8 * np.sin(3 * x_rotated[i]) * np.cos(2 * x_rotated[i]) + \
                     0.4 * np.sin(5 * x_rotated[i]) * np.cos(4 * x_rotated[i])
            
        # Add radial basis function components with different centers and widths
        centers = np.linspace(-3, 3, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            result += 0.6 * np.exp(-0.5 * ((x_rotated[0] - center)**2 + (x_rotated[1] - center)**2)) + \
                     0.3 * np.exp(-0.3 * ((x_rotated[0] - center)**2 + (x_rotated[1] - center)**2))
            
        # Add cross-dimensional coupling with asymmetric interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                result += 0.2 * np.sin(x_rotated[i]) * np.cos(x_rotated[j]) * \
                         np.exp(-0.1 * (x_rotated[i]**2 + x_rotated[j]**2)) + \
                         0.15 * np.cos(x_rotated[i]) * np.sin(x_rotated[j])
                
        # Add a non-smooth component with step-like behavior and noise
        result += 0.25 * np.sum(np.abs(x)**1.3) + 0.1 * np.sum(np.floor(np.abs(x)) * np.cos(x))
        
        # Add a highly oscillatory component with exponential decay
        for i in range(self.dim):
            result += 0.4 * np.sin(15 * x_rotated[i]) * np.exp(-0.2 * np.abs(x_rotated[i])) + \
                     0.3 * np.cos(20 * x_rotated[i]) * np.exp(-0.1 * np.sum(x**2))
        
        # Add a component with fractional powers and asymmetric coupling
        for i in range(self.dim):
            result += 0.22 * (np.abs(x_rotated[i])**1.7) * np.sin(3 * x_rotated[i]) + \
                     0.18 * (x_rotated[i]**3) * np.cos(2 * x_rotated[i])
            
        # Add a component with multiple local minima using sinusoidal modulation
        for i in range(self.dim):
            result += 0.35 * np.sin(7 * x_rotated[i]) * np.cos(8 * x_rotated[i]) * \
                     np.exp(-0.15 * np.abs(x_rotated[i])) + \
                     0.25 * np.sin(4 * x_rotated[i]**2) * np.cos(3 * x_rotated[i]**3)
            
        # Add small random noise to prevent trivial solutions
        result += 0.005 * np.random.random()
        
        return result