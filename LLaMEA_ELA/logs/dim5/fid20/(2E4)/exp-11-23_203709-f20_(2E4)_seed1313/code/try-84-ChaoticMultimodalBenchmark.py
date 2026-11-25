import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive elliptic component with chaotic orientation and dynamic scaling
        elliptic = 0
        for i in range(self.dim):
            a = 1.0 + 0.4 * np.sin(0.6 * i + 1.2)
            b = 1.0 + 0.4 * np.cos(0.6 * i + 1.2)
            theta = 0.15 * i + 0.3 * np.sin(0.4 * i)
            cos_theta = np.cos(theta)
            sin_theta = np.sin(theta)
            x_rot = cos_theta * x[i] - sin_theta * x[(i+1) % self.dim]
            y_rot = sin_theta * x[i] + cos_theta * x[(i+1) % self.dim]
            elliptic += (x_rot**2 / a**2 + y_rot**2 / b**2) * np.exp(-0.08 * (x[i]**2 + x[(i+1) % self.dim]**2))
        
        # Chaotic trigonometric coupling with dynamic frequencies and cross-dimensional interactions
        trig_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 2.5 + 0.6 * np.sin(0.5 * i)
                freq_j = 2.5 + 0.6 * np.cos(0.5 * j)
                dx = x[i] - x[j]
                trig_coupling += np.sin(freq_i * dx) * np.cos(freq_j * dx) * (1.0 + 0.3 * np.abs(dx)) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Stochastic perturbation with chaotic amplitude modulation and temporal correlation
        stochastic = 0
        for i in range(self.dim):
            amp = 0.4 + 0.5 * np.sin(1.7 * i + 0.6)
            noise = np.random.normal(0, 1)
            stochastic += amp * noise * np.exp(-0.12 * x[i]**2)
        
        # Polynomial chaos expansion with varying coefficients and higher-order terms
        poly = 0
        for i in range(self.dim):
            deg = 3 + int(4 * np.sin(0.7 * i + 0.6))
            coeff = 1.2 + 0.6 * np.cos(0.8 * i)
            bias = -1.2 + 2.4 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            poly += coeff * (x[i] - bias)**deg
        
        # Radial basis function interactions with dynamic centers and widths
        rbf = 0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.8 * i + 0.7)
            width = 0.5 + 0.3 * np.cos(0.9 * i)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Cross-dimensional coupling with chaotic phase shifts
        cross_coupling = 0
        for i in range(self.dim):
            phase_shift = 0.2 * np.sin(1.3 * i + 0.8)
            cross_coupling += np.sin(x[i] + phase_shift) * np.cos(x[(i+2) % self.dim] + phase_shift) * (1.0 + 0.1 * np.abs(x[i]))
        
        # Dimensionality scaling with chaotic conditioning and exponential weighting
        dim_scaling = np.sum(np.exp(0.2 * np.arange(self.dim))) / self.dim
        
        # Combine all components with optimized weights
        return 2.0 * elliptic + 1.5 * trig_coupling + 0.8 * stochastic + 0.5 * poly + 1.0 * rbf + 0.9 * cross_coupling + 12.0 * dim_scaling