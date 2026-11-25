import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Elliptic component with adaptive axes and orientation
        elliptic = 0
        for i in range(self.dim):
            a = 1.0 + 0.5 * np.sin(0.7 * i)
            b = 1.0 + 0.5 * np.cos(0.7 * i)
            theta = 0.2 * i
            cos_theta = np.cos(theta)
            sin_theta = np.sin(theta)
            x_rot = cos_theta * x[i] - sin_theta * x[(i+1) % self.dim]
            y_rot = sin_theta * x[i] + cos_theta * x[(i+1) % self.dim]
            elliptic += (x_rot**2 / a**2 + y_rot**2 / b**2) * np.exp(-0.1 * (x[i]**2 + x[(i+1) % self.dim]**2))
        
        # Trigonometric coupling between dimensions
        trig_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                trig_coupling += np.sin(3.0 * dx) * np.cos(2.0 * dx) * (1.0 + 0.1 * np.abs(dx))
        
        # Stochastic perturbation component with chaotic amplitude modulation
        stochastic = 0
        for i in range(self.dim):
            amp = 0.5 + 0.5 * np.sin(1.3 * i + 1.0)
            stochastic += amp * np.random.normal(0, 1) * np.exp(-0.05 * x[i]**2)
        
        # Polynomial landscape with varying degree and bias
        poly = 0
        for i in range(self.dim):
            deg = 3 + int(2 * np.sin(0.5 * i))
            bias = -2.0 + 4.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            poly += (x[i] - bias)**deg
        
        # Dimensionality scaling with chaotic conditioning
        dim_scaling = np.sum(np.exp(0.2 * np.arange(self.dim))) / self.dim
        
        # Combine all components
        return 2.0 * elliptic + 1.5 * trig_coupling + 0.8 * stochastic + 0.6 * poly + 15.0 * dim_scaling