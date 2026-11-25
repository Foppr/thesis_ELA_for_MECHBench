import numpy as np

class QuaternionPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for quaternion-like interactions
        self.rotation_matrix = np.random.rand(dim, dim) * 2 - 1
        self.rotation_matrix = np.dot(self.rotation_matrix, self.rotation_matrix.T)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial with mixed degrees
        result = 0.1 * np.sum(x**6) + 0.3 * np.sum(x**4) + 0.5 * np.sum(x**2)
        
        # Add radial basis function components with varying widths and centers
        centers = np.linspace(-3, 3, min(8, self.dim))
        for i in range(min(8, self.dim)):
            if i < len(centers):
                rbf_term = np.exp(-0.5 * np.sum((x - centers[i])**2) / (0.5 + 0.1 * i))
                result += 0.8 * rbf_term * np.sin(3 * x[i])
        
        # Add quaternion-inspired coupling terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quaternion-like interaction using rotation matrix
                rot_x = np.dot(self.rotation_matrix, x)
                interaction = (x[i] * rot_x[j] - x[j] * rot_x[i])**2
                result += 0.2 * interaction * np.cos(x[i] + x[j])
        
        # Add chaotic polynomial components with varying exponents
        for i in range(self.dim):
            # Fractional polynomial with chaotic exponent modulation
            exp_mod = 1.5 + 0.8 * np.sin(i * 0.7)
            result += 0.3 * (x[i]**exp_mod) * np.cos(2 * x[i]) + \
                     0.2 * (x[i]**(exp_mod * 0.7)) * np.sin(5 * x[i])
        
        # Add multi-modal sine-cosine combinations
        for i in range(self.dim):
            result += 0.4 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * \
                     np.exp(-0.1 * x[i]**2) + \
                     0.3 * np.cos(15 * x[i]) * np.sin(8 * x[i]) * \
                     np.exp(-0.05 * x[i]**2)
        
        # Add a non-smooth component with step-like behavior
        result += 0.25 * np.sum(np.abs(x)**1.3) + \
                 0.15 * np.sum(np.floor(np.abs(x)) * np.cos(2 * x))
        
        # Add cross-dimensional polynomial coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = (x[i]**3) * (x[j]**2) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                result += 0.2 * coupling * np.sin(x[i] * x[j])
        
        # Add a complex oscillatory term with dynamic frequency
        freq = 2.0 + 1.5 * np.sin(np.sum(x) * 0.3)
        result += 0.3 * np.sin(freq * np.sum(x)) * np.cos(0.5 * np.sum(x**2))
        
        # Add noise to prevent trivial solutions
        result += 0.01 * np.random.random()
        
        return result