import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced adaptive elliptic component with chaotic orientation and dynamic scaling
        elliptic = 0
        for i in range(self.dim):
            a = 1.0 + 0.5 * np.sin(0.7 * i + 1.3)
            b = 1.0 + 0.5 * np.cos(0.7 * i + 1.3)
            theta = 0.2 * i + 0.4 * np.sin(0.5 * i)
            cos_theta = np.cos(theta)
            sin_theta = np.sin(theta)
            x_rot = cos_theta * x[i] - sin_theta * x[(i+1) % self.dim]
            y_rot = sin_theta * x[i] + cos_theta * x[(i+1) % self.dim]
            elliptic += (x_rot**2 / a**2 + y_rot**2 / b**2) * np.exp(-0.1 * (x[i]**2 + x[(i+1) % self.dim]**2))
        
        # Enhanced chaotic trigonometric coupling with dynamic frequencies and cross-dimensional interactions
        trig_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 3.0 + 0.7 * np.sin(0.6 * i)
                freq_j = 3.0 + 0.7 * np.cos(0.6 * j)
                dx = x[i] - x[j]
                trig_coupling += np.sin(freq_i * dx) * np.cos(freq_j * dx) * (1.0 + 0.4 * np.abs(dx)) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
        
        # Enhanced stochastic perturbation with chaotic amplitude modulation and temporal correlation
        stochastic = 0
        for i in range(self.dim):
            amp = 0.5 + 0.6 * np.sin(1.8 * i + 0.7)
            noise = np.random.normal(0, 1)
            stochastic += amp * noise * np.exp(-0.15 * x[i]**2)
        
        # Enhanced polynomial chaos expansion with varying coefficients and higher-order terms
        poly = 0
        for i in range(self.dim):
            deg = 4 + int(3 * np.sin(0.8 * i + 0.7))
            coeff = 1.5 + 0.7 * np.cos(0.9 * i)
            bias = -1.5 + 3.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            poly += coeff * (x[i] - bias)**deg
        
        # Enhanced radial basis function interactions with dynamic centers and widths
        rbf = 0
        for i in range(self.dim):
            center = 2.5 * np.sin(0.9 * i + 0.8)
            width = 0.6 + 0.4 * np.cos(1.0 * i)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Enhanced cross-dimensional coupling with chaotic phase shifts
        cross_coupling = 0
        for i in range(self.dim):
            phase_shift = 0.3 * np.sin(1.4 * i + 0.9)
            cross_coupling += np.sin(x[i] + phase_shift) * np.cos(x[(i+2) % self.dim] + phase_shift) * (1.0 + 0.2 * np.abs(x[i]))
        
        # Enhanced dimensionality scaling with chaotic conditioning and exponential weighting
        dim_scaling = np.sum(np.exp(0.25 * np.arange(self.dim))) / self.dim
        
        # Combine all components with optimized weights for improved fitness
        return 2.5 * elliptic + 1.8 * trig_coupling + 0.9 * stochastic + 0.6 * poly + 1.2 * rbf + 1.1 * cross_coupling + 13.0 * dim_scaling