import numpy as np

class GaussianRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian mixture centers and weights for different scales
        self.centers = np.random.uniform(-1, 1, (10, dim))
        self.weights = np.random.exponential(1, 10)
        self.weights /= np.sum(self.weights)
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Gaussian mixture component with varying scales and orientations
        gaussian_sum = 0.0
        for i in range(10):
            center = self.centers[i]
            weight = self.weights[i]
            # Varying covariance matrix with rotation and scaling
            scale = 0.5 + 1.5 * np.random.rand()
            angle = np.random.rand() * 2 * np.pi
            cos_a, sin_a = np.cos(angle), np.sin(angle)
            cov = np.array([[scale, 0], [0, scale/2]])
            rot = np.array([[cos_a, -sin_a], [sin_a, cos_a]])
            cov = rot @ cov @ rot.T
            
            # Multivariate Gaussian
            diff = x_scaled - center
            inv_cov = np.linalg.inv(cov)
            det_cov = np.linalg.det(cov)
            gaussian_sum += weight * np.exp(-0.5 * diff @ inv_cov @ diff) / np.sqrt(det_cov)
        
        # Sinusoidal modulation with polynomial interaction terms
        sinusoidal = 0.0
        for i in range(self.dim):
            # Multi-frequency sine waves with varying amplitudes
            freqs = [1.0, 2.0, 3.0, 4.0, 5.0]
            amps = [1.0, 0.8, 0.6, 0.4, 0.2]
            for freq, amp in zip(freqs, amps):
                sinusoidal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Polynomial interaction terms with varying degrees and coefficients
        polynomial = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Interaction terms of different degrees
                poly_term = (x_scaled[i]**2 + x_scaled[j]**2) * (x_scaled[i] * x_scaled[j])**3
                polynomial += poly_term * (0.5 + 0.5 * np.sin(0.5 * (i + j)))
        
        # Ridge-like structure with varying widths and heights
        ridge = 0.0
        for i in range(self.dim):
            # Multiple ridges with different orientations and curvatures
            ridge += (np.sin(x_scaled[i] * 2) + 0.5 * np.cos(x_scaled[i] * 3)) * \
                     np.exp(-0.5 * x_scaled[i]**2)
        
        # Combine all components with dynamic weights
        return 1.5 * gaussian_sum + 2.0 * sinusoidal + 1.2 * polynomial + 0.8 * ridge