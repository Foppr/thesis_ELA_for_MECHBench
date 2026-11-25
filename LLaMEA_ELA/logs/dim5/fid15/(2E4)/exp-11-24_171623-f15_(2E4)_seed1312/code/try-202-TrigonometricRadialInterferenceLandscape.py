import numpy as np

class TrigonometricRadialInterferenceLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Modified polynomial chaos coefficients with increased randomness
        self.poly_coeffs = np.array([1.5 + 0.3 * np.cos(i * np.pi / dim) for i in range(dim)])
        # Adjusted quaternion weights with stronger coupling
        self.quat_weights = np.array([np.cos(2 * i * np.pi / (dim + 2)) + 1j * np.sin(2 * i * np.pi / (dim + 2)) for i in range(dim)])
        # Modified radial basis centers and widths for increased complexity
        self.centers = np.random.uniform(-0.8, 0.8, dim)
        self.widths = np.random.uniform(0.3, 1.5, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Modified Gaussian radial basis component with enhanced interference
        gaussian_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.centers[i])**2)
            gaussian_sum += np.exp(-0.3 * dist / (self.widths[i]**2)) * np.cos(3 * x_norm[i])
        
        # Modified polynomial chaos expansion component with higher-order terms
        poly_sum = 0.0
        for i in range(self.dim):
            poly_term = self.poly_coeffs[i] * x_norm[i]**4 - 0.6 * x_norm[i]**2 + 0.1
            poly_sum += poly_term * np.sin(4 * x_norm[i])
        
        # Enhanced quaternion-inspired cross-dimensional coupling
        quat_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Stronger quaternion-like interaction term
                q_i = self.quat_weights[i]
                q_j = self.quat_weights[j]
                interaction = np.real(q_i * np.conj(q_j) * (x_norm[i] + 1j * x_norm[j]))
                quat_sum += interaction * np.exp(-0.7 * (interaction)**2)
        
        # Modified multi-modal harmonic component with varying frequencies
        harm_sum = 0.0
        for i in range(self.dim):
            freq = 5.0 + 0.5 * np.cos(i * np.pi / self.dim)
            amp = 1.2 + 0.2 * np.sin(i * np.pi / self.dim)
            harm_sum += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] / 2)
        
        # Adjusted basin structure with sharper potential wells
        basin_sum = 0.0
        for i in range(self.dim):
            if x_norm[i] < 0:
                basin_sum += (x_norm[i]**7 - 0.8 * x_norm[i]**5 + 0.3 * x_norm[i]**3) * np.exp(-0.4 * x_norm[i]**2)
            else:
                basin_sum += (x_norm[i]**6 - 0.7 * x_norm[i]**4 + 0.25 * x_norm[i]**2) * np.exp(-0.2 * x_norm[i]**2)
        
        # Combined landscape with modified scaling factors
        result = 0.3 * gaussian_sum + 0.15 * poly_sum + 0.3 * quat_sum + 0.15 * harm_sum + 0.1 * basin_sum
        
        # Enhanced conditioning factor based on dimensionality and input magnitude
        condition_factor = 1.0 + 0.7 * np.log(self.dim + 2)
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.4 * np.abs(x_norm[i]) + 0.15 * x_norm[i]**5 + 0.08 * np.sin(4 * x_norm[i]))
        
        # Final transformation with global scaling and noise modulation
        noise = 0.08 * np.sum(np.cos(x_norm * 9))
        return result * condition_factor + noise + 0.15 * np.sum(x_norm**9)