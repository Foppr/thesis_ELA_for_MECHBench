import numpy as np

class ExponentialTrigonometricSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced exponential barrier parameters with increased variability and complexity
        self.barrier_centers = -2.0 + 4.0 * np.random.rand(dim)
        self.barrier_heights = 1.5 + 5.0 * np.random.rand(dim)
        self.barrier_widths = 0.2 + 1.8 * np.random.rand(dim)
        # Modified trigonometric coupling with higher frequencies and interaction terms
        self.coupling_amplitudes = 2.0 + 4.0 * np.random.rand(dim, dim)
        self.coupling_frequencies = 4.0 + 10.0 * np.random.rand(dim, dim)
        # Adjusted saddle point configurations with more complex attraction patterns
        self.saddle_positions = 3.0 * np.random.rand(dim, 15) - 1.5
        self.saddle_strengths = 0.8 + 4.0 * np.random.rand(15)
        # Asymmetric polynomial terms with varied exponents and coefficients
        self.poly_exponents = 2.0 + 6.0 * np.random.rand(dim)
        self.poly_coefficients = 0.3 + 3.0 * np.random.rand(dim)
        # Global rotation matrix with more complex transformation
        angle = np.pi * np.random.rand()
        cos_angle, sin_angle = np.cos(angle), np.sin(angle)
        self.rotation_matrix = np.array([[cos_angle, -sin_angle], [sin_angle, cos_angle]])
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential barrier component with multiple peaks
        barrier_sum = 0.0
        for i in range(self.dim):
            dist = np.abs(x_norm[i] - self.barrier_centers[i])
            barrier_sum += self.barrier_heights[i] * np.exp(-0.5 * (dist / self.barrier_widths[i])**2)
        
        # Modified trigonometric coupling with cross-terms and phase shifts
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_amplitudes[i, j] * np.sin(self.coupling_frequencies[i, j] * x_norm[i] + 0.5 * x_norm[j]) * np.cos(x_norm[j] + 0.3 * x_norm[i])
        
        # Enhanced saddle point attraction with more complex interactions
        saddle_sum = 0.0
        for k in range(15):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.saddle_positions[i, k])**2
            saddle_sum += self.saddle_strengths[k] * np.exp(-dist / 2.0)
        
        # Asymmetric polynomial component with different exponents and scaling
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += self.poly_coefficients[i] * np.power(np.abs(x_norm[i]), self.poly_exponents[i])
        
        # Combine all components with optimized weights
        result = 0.25 * barrier_sum + 0.30 * coupling_sum + 0.25 * saddle_sum + 0.20 * poly_sum
        
        # Add rotation and conditioning effects with more complex transformation
        if self.dim >= 2:
            rotated = np.dot(self.rotation_matrix, x_norm[:2])
            result += 0.10 * (rotated[0]**3 + rotated[1]**3)
        
        # Improved penalty term with higher-order polynomial and adaptive scaling
        penalty = 0.10 * np.sum(np.abs(x_norm)**5)
        
        return result + penalty