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
            chaotic_factor = 1.0 + 0.3 * np.sin(r) * np.cos(r * 2.0) * np.sin(r * 3.0)
            result += (r**3.0) * chaotic_factor * np.exp(-r**2 / 25.0)
        
        # Cross-dimensional quaternion coupling with imaginary components
        for i in range(self.dim):
            xi = x[i]
            quat_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    xj = x[j]
                    # Quaternion-inspired coupling with complex frequency modulation
                    freq_real = 1.0 + 0.4 * np.sin(xi) * np.cos(xj)
                    freq_imag = 0.3 * np.cos(xi) * np.sin(xj)
                    quat_sum += (np.sin(freq_real * xi + freq_imag * xj) * 
                                np.cos(freq_real * xj + freq_imag * xi))
            result += 0.4 * quat_sum * np.exp(-abs(xi) / 3.0)
        
        # Multi-scale chaotic modulation with exponential decay
        for scale in [1, 2, 3, 4]:
            scale_factor = 1.0 / (scale ** 2.0)
            freq = scale * (1.0 + 0.5 * np.sin(r / 3.0) * np.cos(r / 2.0))
            chaotic_term = np.sin(freq * r) * np.cos(freq * r) * np.exp(-r**2 / (20.0 * scale))
            result += scale_factor * chaotic_term
        
        # Polynomial perturbations with saddle-point dominance
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Septic polynomial with chaotic coefficients to create multiple extrema
            coeff1 = 1.0 + 0.2 * np.sin(xi)
            coeff2 = 7.0 + 0.5 * np.cos(xi)
            poly_term = coeff1 * xi**7 - coeff2 * xi**5 + 30*xi**3 - 60*xi
            poly_sum += poly_term * np.exp(-abs(xi) / 2.5)
        result += 0.6 * poly_sum
        
        # Adaptive noise with chaotic amplitude modulation
        noise_amp = 0.15 * (1.0 + 0.4 * np.sin(r) * np.cos(r * 1.5))
        noise = np.random.normal(0, noise_amp, self.dim)
        noise_component = np.sum(noise**2) * np.exp(-r**2 / 35.0)
        result += noise_component
        
        # Angular coupling with chaotic weighting
        angular_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic angular modulation with multiple frequency components
            angular_term = (np.sin(3.0 * xi) * np.cos(2.0 * xi) + 
                           0.3 * np.sin(xi) * np.cos(4.0 * xi) + 
                           0.5 * np.sin(2.0 * xi))
            angular_sum += angular_term * np.exp(-xi**2 / 12.0)
        result += 0.5 * angular_sum
        
        # Fractal frequency modulation with higher-order harmonics
        fractal_freq = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Add higher-order harmonic components to increase complexity
            fractal_freq += (np.sin(5.0 * xi) * np.cos(3.0 * xi) + 
                           0.2 * np.sin(7.0 * xi) * np.cos(4.0 * xi) +
                           0.1 * np.sin(9.0 * xi))
        result += 0.3 * fractal_freq * np.exp(-r**2 / 50.0)
        
        # Higher-order polynomial perturbations
        higher_order_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Add octic and decic terms to increase multimodality
            coeff3 = 1.0 + 0.1 * np.sin(xi**2)
            coeff4 = 10.0 + 0.3 * np.cos(xi**2)
            higher_order_term = coeff3 * xi**8 - coeff4 * xi**6 + 50*xi**4 - 100*xi**2 + 20
            higher_order_sum += higher_order_term * np.exp(-abs(xi) / 3.0)
        result += 0.7 * higher_order_sum
        
        # Final chaotic normalization
        result = result / (1.0 + 0.03 * r**2) * (1.0 + 0.1 * np.sin(r * 4.0))
        
        return result