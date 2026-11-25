import numpy as np

class ChaoticQuaternionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic radial landscape with quaternion-inspired coupling
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            # Quaternion-inspired radial pattern with chaotic modulation
            chaotic_factor = 1.0 + 0.5 * np.sin(r) * np.cos(r * 2.0) * np.sin(r * 3.0)
            result += (r**3.0) * chaotic_factor * np.exp(-r**2 / 25.0)
        
        # Cross-dimensional quaternion coupling with imaginary components
        for i in range(self.dim):
            xi = x[i]
            quat_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    xj = x[j]
                    # Quaternion-inspired coupling with complex frequency modulation
                    freq_real = 1.0 + 0.6 * np.sin(xi) * np.cos(xj)
                    freq_imag = 0.4 * np.cos(xi) * np.sin(xj)
                    quat_sum += (np.sin(freq_real * xi + freq_imag * xj) * 
                                np.cos(freq_real * xj + freq_imag * xi))
            result += 0.6 * quat_sum * np.exp(-abs(xi) / 3.0)
        
        # Multi-scale chaotic modulation with exponential decay
        for scale in [1, 2, 3, 4, 5]:
            scale_factor = 1.0 / (scale ** 2.5)
            freq = scale * (1.0 + 0.6 * np.sin(r / 3.0) * np.cos(r / 2.0))
            chaotic_term = np.sin(freq * r) * np.cos(freq * r) * np.exp(-r**2 / (20.0 * scale))
            result += scale_factor * chaotic_term
        
        # Polynomial perturbations with saddle-point dominance
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Septic polynomial with chaotic coefficients to create multiple extrema
            coeff1 = 1.0 + 0.3 * np.sin(xi)
            coeff2 = 7.0 + 0.6 * np.cos(xi)
            poly_term = coeff1 * xi**7 - coeff2 * xi**5 + 35*xi**3 - 65*xi
            poly_sum += poly_term * np.exp(-abs(xi) / 2.5)
        result += 0.8 * poly_sum
        
        # Adaptive noise with chaotic amplitude modulation
        noise_amp = 0.2 * (1.0 + 0.5 * np.sin(r) * np.cos(r * 1.5))
        noise = np.random.normal(0, noise_amp, self.dim)
        noise_component = np.sum(noise**2) * np.exp(-r**2 / 35.0)
        result += noise_component
        
        # Angular coupling with chaotic weighting
        angular_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic angular modulation with multiple frequency components
            angular_term = (np.sin(4.0 * xi) * np.cos(2.0 * xi) + 
                           0.4 * np.sin(xi) * np.cos(5.0 * xi) + 
                           0.6 * np.sin(2.0 * xi))
            angular_sum += angular_term * np.exp(-xi**2 / 12.0)
        result += 0.7 * angular_sum
        
        # Final chaotic normalization
        result = result / (1.0 + 0.05 * r**2) * (1.0 + 0.15 * np.sin(r * 4.0))
        
        return result