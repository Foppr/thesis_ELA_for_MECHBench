import numpy as np

class GaussianPolynomialQuaternionLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients and quaternion weights
        self.poly_coeffs = np.array([1.0 + 0.5 * np.sin(i * np.pi / dim) for i in range(dim)])
        self.quat_weights = np.array([np.cos(i * np.pi / (dim + 1)) + 1j * np.sin(i * np.pi / (dim + 1)) for i in range(dim)])
        # Precompute radial basis centers and widths
        self.centers = np.random.uniform(-1, 1, dim)
        self.widths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Gaussian radial basis component with multi-scale influence
        gaussian_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.centers[i])**2)
            gaussian_sum += np.exp(-0.5 * dist / (self.widths[i]**2)) * np.sin(2 * np.pi * x_norm[i])
        
        # Polynomial chaos expansion component
        poly_sum = 0.0
        for i in range(self.dim):
            poly_term = self.poly_coeffs[i] * x_norm[i]**3 - 0.5 * x_norm[i]
            poly_sum += poly_term * np.cos(3 * x_norm[i])
        
        # Quaternion-inspired cross-dimensional coupling
        quat_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quaternion-like interaction term
                q_i = self.quat_weights[i]
                q_j = self.quat_weights[j]
                interaction = np.real(q_i * np.conj(q_j) * (x_norm[i] + 1j * x_norm[j]))
                quat_sum += interaction * np.exp(-0.5 * (interaction)**2)
        
        # Multi-modal harmonic component with varying amplitudes
        harm_sum = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.3 * np.sin(i * np.pi / self.dim)
            harm_sum += amp * np.sin(4 * x_norm[i]) * np.cos(2 * x_norm[i])
        
        # Basin structure with polynomial potential wells
        basin_sum = 0.0
        for i in range(self.dim):
            if x_norm[i] < 0:
                basin_sum += (x_norm[i]**6 - 0.7 * x_norm[i]**4 + 0.2 * x_norm[i]**2) * np.exp(-0.5 * x_norm[i]**2)
            else:
                basin_sum += (x_norm[i]**5 - 0.6 * x_norm[i]**3 + 0.1 * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Combined landscape with adaptive scaling
        result = 0.25 * gaussian_sum + 0.2 * poly_sum + 0.25 * quat_sum + 0.2 * harm_sum + 0.1 * basin_sum
        
        # Enhanced conditioning factor based on dimensionality and input magnitude
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.2 * np.abs(x_norm[i]) + 0.08 * x_norm[i]**4 + 0.03 * np.sin(3 * x_norm[i]))
        
        # Enhanced noise modulation with dynamic scaling
        noise = 0.03 * np.sum(np.sin(x_norm * 7))
        noise += 0.02 * np.sum(np.cos(x_norm * 5))
        
        # Final transformation with global scaling and improved conditioning
        return result * condition_factor + noise + 0.08 * np.sum(x_norm**8) + 0.01 * np.sum(np.abs(x_norm)**3)