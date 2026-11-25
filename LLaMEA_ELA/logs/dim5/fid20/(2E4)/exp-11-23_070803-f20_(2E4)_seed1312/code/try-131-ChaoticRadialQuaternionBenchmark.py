import numpy as np

class ChaoticRadialQuaternionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic logistic map component with dimensionally varying parameters
        chaotic_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Logistic map with time-varying r parameter based on dimension index
            r = 3.95 + 0.05 * np.sin(i * np.pi / self.dim)
            logistic_value = r * xi * (1 - xi)
            chaotic_component += logistic_value * (1 + 0.2 * np.cos(i))
        
        # Radial basis function component with adaptive centers and widths
        rbf_component = 0
        num_centers = min(8, self.dim)
        for i in range(num_centers):
            center = np.sin(i * np.pi / num_centers) * 0.8
            width = 0.5 + 0.3 * np.cos(i * np.pi / num_centers)
            # Radial distance with dimensionally weighted contributions
            dist = np.sum((x_norm - center)**2)
            rbf_component += np.exp(-dist / (2 * width**2)) * (1 + 0.15 * np.sin(i))
        
        # Quaternion-inspired rotational symmetry component
        quat_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Create rotational invariance with sine-cosine combinations
            angle = i * np.pi / self.dim
            rot_term = np.sin(xi * np.cos(angle)) + np.cos(xi * np.sin(angle))
            quat_component += rot_term * (1 + 0.25 * np.cos(i * 2))
        
        # Cross-dimensional interaction with hyperbolic tangent coupling
        cross_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Hyperbolic tangent based coupling with varying strength
                strength = 0.4 + 0.3 * np.sin((i + j) * np.pi / (self.dim + 1))
                coupling = strength * np.tanh(x_norm[i] + x_norm[j]) * np.tanh(x_norm[i] - x_norm[j])
                cross_component += coupling * (1 + 0.1 * np.sin(i * j))
        
        # Multi-scale oscillatory component with fractal-like frequency modulation
        oscillatory_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple frequency harmonics with dimensionally modulated amplitudes
            frequencies = [1, 2, 4, 8, 16]
            for k, freq in enumerate(frequencies):
                amp = 0.7 + 0.3 * np.sin(i * freq * np.pi / self.dim)
                oscillatory_component += amp * np.sin(freq * xi) * (1 + 0.1 * np.cos(freq * i))
        
        # Asymmetric potential with polynomial and exponential terms
        asymmetric_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Combination of polynomial and exponential terms creating multiple minima
            asymmetric_component += (xi**6 - 3*xi**4 + 2*xi**2) * (1 + 0.2 * np.sin(i)) + \
                                   0.5 * np.exp(-xi**2) * (1 + 0.3 * np.cos(i)) + \
                                   0.1 * xi**7 * np.sin(xi)
        
        # Adaptive weighting based on dimension
        weights = np.array([1.0 + 0.2 * np.sin(i * np.pi / self.dim) for i in range(self.dim)])
        weighted_sum = np.sum(weights * x_norm**2) / self.dim
        
        # Combine all components with dynamic scaling
        result = 1.2 * chaotic_component + 0.9 * rbf_component + 1.1 * quat_component + \
                0.8 * cross_component + 1.0 * oscillatory_component + 0.7 * asymmetric_component + \
                0.3 * weighted_sum
        
        # Add controlled noise with dynamic amplitude
        noise_amplitude = 0.005 + 0.003 * np.cos(np.sum(x_norm))
        noise = np.random.normal(0, noise_amplitude)
        
        return result + noise