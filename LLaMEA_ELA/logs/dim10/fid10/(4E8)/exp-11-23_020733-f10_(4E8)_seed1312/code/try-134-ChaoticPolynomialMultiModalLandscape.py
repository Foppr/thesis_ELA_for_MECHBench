import numpy as np

class ChaoticPolynomialMultiModalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for different dimensions
        self.chaotic_params = [0.5 + 0.4 * np.sin(i * np.pi / (self.dim + 1)) for i in range(self.dim)]
        self.rbf_centers = [np.random.uniform(-5.0, 5.0) for _ in range(self.dim)]
        self.poly_coeffs = [1.0 + 0.5 * np.cos(i * np.pi / (self.dim + 2)) for i in range(self.dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term
        result = 0.1 * np.sum(x**2)
        
        # Chaotic coupling with dimensionally varying parameters
        for i in range(self.dim):
            chaotic_factor = self.chaotic_params[i]
            result += 3.0 * (x[i]**2) * np.sin(chaotic_factor * x[i])**2 + 2.0 * np.cos(chaotic_factor * x[i])**2
        
        # Dynamic radial basis functions with adaptive centers
        for i in range(self.dim):
            rbf_term = 0.0
            for j in range(min(5, self.dim)):
                center = self.rbf_centers[j] if j < len(self.rbf_centers) else np.random.uniform(-5.0, 5.0)
                sigma = 0.5 + 0.3 * np.sin(i * j * np.pi / (self.dim + 1))
                rbf_term += np.exp(-((x[i] - center)**2) / (2 * sigma**2))
            result += 1.5 * rbf_term
        
        # Adaptive polynomial chaos expansions with varying coefficients
        for i in range(self.dim):
            poly_expansion = 0.0
            for k in range(1, min(4, self.dim + 1)):
                coeff = self.poly_coeffs[i] * np.sin(k * x[i])
                poly_expansion += coeff * (x[i]**k)
            result += 0.8 * poly_expansion
        
        # Multi-scale periodic potential with chaotic modulation
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.cos(i * np.pi / (self.dim + 2))
            modulator = 0.5 + 0.5 * np.sin(i * x[i] * np.pi / (self.dim + 1))
            result += 4.0 * np.sin(scale * x[i])**3 * modulator + 1.5 * np.cos(scale * x[i])**2
        
        # Cross-dimensional coupling with chaotic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x[i] - x[j])
                chaotic_coupling = 0.3 * np.sin(dist)**3 + 0.2 * np.cos(dist)**2
                result += chaotic_coupling * (1.0 + 0.5 * np.sin(i * j))
        
        # Boundary-induced chaotic tunneling effect
        boundary_effect = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.0:
                penalty = 3.0 * (abs(x[i]) - 4.0)**2 * np.exp(-abs(x[i])**2 / 30.0)
                boundary_effect += penalty
        result += boundary_effect
        
        # Global chaotic phase modulation
        global_phase = np.sin(np.sum(x) * np.pi / (self.dim + 1)) * np.cos(np.sum(x) * np.pi / (self.dim + 3))
        result *= (1.0 + 0.4 * global_phase)
        
        return result