import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic rotation matrix for dimensionality
        self.rotation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                self.rotation_matrix[i, j] = np.sin(i * 0.7 + j * 0.3) * np.cos(i * 0.5 + j * 0.8)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply chaotic rotation to create non-separable structure
        x_rotated = self.rotation_matrix @ x
        
        # Separable quadratic base with variable conditioning
        result = 0.5 * np.sum(x**2)
        
        # Add chaotic sine-cosine interactions with logistic map modulation
        for i in range(self.dim):
            # Logistic map for dynamic frequency modulation
            freq = 3.8 * np.sin(i * 0.5) * (1 - np.sin(i * 0.5)) + 1.5
            amp = 1.2 + 0.4 * np.sin(i * 0.8)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Add asymmetric saddle points with varying steepness and chaotic coefficients
        for i in range(self.dim):
            # Chaotic coefficient modulation using sine-cosine products
            coeff1 = 0.1 + 0.05 * np.sin(i * 1.3)
            coeff2 = 0.05 + 0.03 * np.cos(i * 1.7)
            result += coeff1 * x[i]**3 + coeff2 * x[i]**4 + 0.03 * np.sin(7 * x[i]) * np.cos(4 * x[i])
        
        # Add long-range coupling terms with exponential decay and chaotic weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic weight modulation using sine products
                weight = 0.2 + 0.1 * np.sin(i * 0.9) * np.cos(j * 0.6)
                coupling = weight * np.exp(-0.3 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
                result += coupling
        
        # Add multi-modal interaction with fractal-like noise using chaotic sine series
        noise = 0.05 * np.sum(np.sin(15 * x) + np.cos(11 * x) + np.tan(8 * x) + 
                              0.3 * np.sin(23 * x) * np.cos(17 * x))
        result += noise
        
        # Add cross-dimensional coupling with chaotic interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                # Chaotic interaction coefficient
                coef = 0.15 + 0.08 * np.sin(i * 0.4) * np.cos(j * 0.3)
                result += coef * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Add chaotic rotation-induced interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                rot_coef = 0.1 + 0.05 * np.sin(i * 0.3) * np.cos(j * 0.7)
                result += rot_coef * x_rotated[i] * x_rotated[j] * np.exp(-0.1 * (x_rotated[i]**2 + x_rotated[j]**2))
        
        # Apply global scaling factor with chaotic modulation
        result *= 1.3 + 0.2 * np.sin(0.5 * self.dim)
        
        return result