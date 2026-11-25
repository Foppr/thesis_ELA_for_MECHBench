import numpy as np

class ChaoticHyperRosenbrockBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base hyper-rosenbrock component with chaotic modulation
        result = 0.0
        for i in range(self.dim - 1):
            xi = x_scaled[i]
            xi1 = x_scaled[i + 1]
            # Chaotic modulation using sine and exponential terms
            modulator = 1.0 + 0.3 * np.sin(10.0 * xi) * np.exp(-xi**2)
            result += modulator * (100.0 * (xi1 - xi**2)**2 + (1.0 - xi)**2)
        
        # Exponential barrier terms creating sharp constraints
        barriers = 0.0
        for i in range(self.dim):
            # Multiple exponential barriers at different positions
            barriers += 5.0 * np.exp(-5.0 * (x_scaled[i] - 0.3)**2) + \
                       3.0 * np.exp(-3.0 * (x_scaled[i] + 0.5)**2) + \
                       2.0 * np.exp(-2.0 * x_scaled[i]**2)
        
        # Multi-scale coupling with fractal-like interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling with varying scales
                scale_factor = 1.0 + 0.5 * np.sin(2.0 * i) * np.cos(3.0 * j)
                coupling += scale_factor * np.sin(5.0 * (x_scaled[i] - x_scaled[j])) * \
                           np.exp(-0.5 * (x_scaled[i] - x_scaled[j])**2)
        
        # Chaotic gradient enhancement with sinusoidal modulation
        chaos = 0.0
        for i in range(self.dim):
            # Add chaotic behavior through higher-order sine terms
            chaos += 0.8 * np.sin(15.0 * x_scaled[i]) * \
                    np.cos(7.0 * x_scaled[i]) * \
                    np.exp(-0.3 * x_scaled[i]**2)
        
        # Combine all components with adaptive weights
        return 0.7 * result + 1.2 * barriers + 0.5 * coupling + 0.3 * chaos