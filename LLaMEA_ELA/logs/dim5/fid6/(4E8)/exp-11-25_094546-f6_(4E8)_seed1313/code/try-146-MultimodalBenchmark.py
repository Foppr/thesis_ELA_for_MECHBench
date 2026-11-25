import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for fractional Brownian motion
        self.hurst = 0.3 + 0.4 * np.random.random()  # Varying Hurst parameter
        self.frac_const = 1.0 / (2.0 * self.hurst)
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Fractional Brownian motion component with dynamic Hurst
        fbm = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Simplified fractional Brownian motion approximation
            fbm += np.sin(2.0 * xi) * np.cos(3.0 * xi) * (1.0 + self.hurst * np.sin(xi))
        
        # Dynamic ridge structure with varying curvature
        ridge = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Ridge with dynamic width and height
            ridge_width = 0.5 + 0.3 * np.sin(0.5 * i)
            ridge_height = 1.0 + 0.7 * np.cos(0.3 * i)
            ridge += ridge_height * np.exp(-0.5 * ((xi - 0.2) / ridge_width)**2)
        
        # High-order non-separable interactions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-separable terms with varying exponents
                exp_factor = 1.0 + 0.5 * np.sin(0.2 * (i + j))
                interaction += (x_norm[i]**exp_factor) * (x_norm[j]**(3.0 - exp_factor)) * np.cos(2.0 * (i + j))
        
        # Dynamic noise component with varying amplitude
        noise_amp = 0.5 + 0.3 * np.sin(self.dim * 0.1)
        noise = 0.0
        for i in range(self.dim):
            noise += noise_amp * np.sin(10.0 * x_norm[i] + i) * np.cos(7.0 * x_norm[i] - i)
        
        # Combined landscape with dynamic scaling
        total = 0.0
        
        # Weighted combination with dynamic weights based on dimensionality
        w1 = 0.3 + 0.2 * np.sin(self.dim * 0.5)  # FBm weight
        w2 = 0.25 + 0.15 * np.cos(self.dim * 0.4)  # Ridge weight
        w3 = 0.35 + 0.2 * np.tanh(self.dim * 0.3)  # Interaction weight
        w4 = 0.1 + 0.05 * np.sin(self.dim * 0.6)   # Noise weight
        
        total += w1 * fbm + w2 * ridge + w3 * interaction + w4 * noise
        
        # Add a global scaling factor based on dimensionality
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return scale_factor * total