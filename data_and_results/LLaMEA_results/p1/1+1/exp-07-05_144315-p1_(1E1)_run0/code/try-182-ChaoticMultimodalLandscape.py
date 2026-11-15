import numpy as np

class ChaoticMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic conditioning factors using logistic map
        self.conditioning_factors = np.zeros(dim)
        x = 0.5
        for i in range(dim):
            x = 3.9 * x * (1 - x)
            self.conditioning_factors[i] = 0.5 + 1.5 * x
            
        # Precompute fractal frequency modulators
        self.frequency_modulators = np.zeros(dim)
        for i in range(dim):
            self.frequency_modulators[i] = 0.1 + 2.9 * np.sin(i * np.pi / (dim + 1)) * np.cos(i * np.pi / (dim + 1))
        
        # Precompute chaotic peak positions
        self.peak_positions = np.zeros(13)
        x = 0.1
        for i in range(13):
            x = 3.8 * x * (1 - x)
            self.peak_positions[i] = -5.0 + 10.0 * x
            
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic polynomial component with dynamic exponents
        poly = 0.0
        for i in range(self.dim):
            exponent = 2.0 + 2.0 * np.sin(i * 0.7 + self.conditioning_factors[i])
            poly += (x[i] ** exponent) * self.conditioning_factors[i]
        
        # Hyperbolic tangent exponential component
        exp_tanh = 0.0
        for i in range(self.dim):
            rate = 0.2 + 0.8 * np.tanh(i * 0.3)
            exp_tanh += np.tanh(rate * np.abs(x[i])) * np.cos(x[i])
        
        # Fractal sinusoidal component with recursive frequency modulation
        sin_fractal = 0.0
        for i in range(self.dim):
            freq = 1.0 + 3.0 * self.frequency_modulators[i]
            amp = 0.3 + 0.7 * np.sin(i * 0.5)
            sin_fractal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        
        # Chaotic valley component with time-delayed feedback
        valley = 0.0
        for i in range(self.dim):
            # Introduce chaotic feedback based on previous dimensions
            feedback = 0.0
            if i > 0:
                feedback = 0.2 * np.sin(x[i-1] * 2.0)
            steepness = 1.0 + 0.8 * np.cos(i * 0.6 + feedback)
            if x[i] >= 0:
                valley += (x[i] ** 2.5) * steepness
            else:
                valley += (x[i] ** 3.5) * steepness
        
        # Multi-scale cross-dimensional interaction with chaotic weights
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use chaotic weight based on both indices
                weight = 0.1 + 0.9 * np.sin(i * j * 0.1 + self.conditioning_factors[i])
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross += weight * np.sin(x[i] * x[j]) * np.exp(-0.2 * dist)
        
        # Chaotic peaks with fractal distribution
        peaks = 0.0
        for center in self.peak_positions:
            width = 0.5 + 0.8 * np.sin(center * 0.4)
            height = 0.8 + 1.2 * np.cos(center * 0.2)
            peaks += height * np.exp(-0.5 * np.sum(((x - center) / width) ** 2))
        
        # Logarithmic and fractional component with chaotic scaling
        frac_log = 0.0
        for i in range(self.dim):
            if x[i] != 0:
                scale = 1.0 + 0.5 * np.sin(i * 0.8)
                frac_log += (np.abs(x[i]) ** (1.5 + 0.5 * np.cos(i * 0.6))) * np.log(np.abs(x[i]) * scale + 1.0)
        
        # Combine all components with chaotic weights
        weights = np.zeros(6)
        x_w = 0.1
        for i in range(6):
            x_w = 3.7 * x_w * (1 - x_w)
            weights[i] = 0.3 + 0.7 * x_w
            
        components = np.array([poly, exp_tanh, sin_fractal, valley, cross, peaks])
        return np.sum(weights * components) + frac_log