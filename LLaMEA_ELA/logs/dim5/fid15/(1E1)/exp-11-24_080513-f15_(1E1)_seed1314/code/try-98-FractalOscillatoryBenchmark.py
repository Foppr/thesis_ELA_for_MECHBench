import numpy as np

class FractalOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Chaotic fractal component with logistic map modulation
        fractal = 0.0
        r = 3.9
        x_prev = 0.5
        for i in range(self.dim):
            x_prev = r * x_prev * (1 - x_prev)
            scale = 1.0 + 0.5 * np.sin(x_prev * 10 * np.pi)
            freq = 5.0 * scale * (i + 1)
            amp = 1.0 / (1.0 + 0.3 * i)
            fractal += amp * np.cos(freq * x_normalized[i]) * np.sin(freq * x_normalized[i])
        
        # Multi-scale oscillatory component with time-varying parameters
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 15.0 + 10.0 * np.sin(i * 0.8)
            amp = 0.4 + 0.6 * np.cos(i * 0.6)
            phase = 0.3 * np.sin(i * 1.1) + 0.2 * np.cos(i * 0.9)
            oscillatory += amp * np.sin(freq * x_normalized[i] + phase) * np.cos(freq * x_normalized[i] + phase)
        
        # Geometric progression interaction terms with chaotic weight modulation
        geometric = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                # Chaotic weight modulation using logistic map
                w = 0.5 + 0.5 * np.sin(dist * 20 * np.pi)
                geometric += w * (x_normalized[i]**2 + x_normalized[j]**2) * np.sin(7 * dist)
        
        # Multi-scale radial basis with chaotic center distribution
        radial = 0.0
        for i in range(self.dim):
            # Chaotic center using logistic map
            center = np.sin(i * 0.5) * np.cos(i * 0.3) + 0.1 * np.sin(i * 15 * np.pi)
            width = 0.1 + 0.4 * np.sin(i * 0.7)
            radial += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2)
        
        # Cross-dimensional coupling with chaotic strength modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic strength modulation
                strength = 0.6 + 0.4 * np.sin(i * 0.5 + j * 0.3 + x_normalized[i] * 5 * np.pi)
                period = 3.0 + 0.8 * np.cos(i * 0.7)
                coupling += strength * np.sin(period * (x_normalized[i] - x_normalized[j])) * np.exp(-0.1 * (x_normalized[i] - x_normalized[j])**2)
        
        # Polynomial interaction with chaotic exponents
        poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic exponent modulation
                exp_mod = 2 + np.sin(i * 0.4 + j * 0.3) * 2
                poly += (x_normalized[i] * x_normalized[j])**(exp_mod)
        
        # Logarithmic noise component with multi-chaotic phase modulation
        noise = 0.0
        r1, r2, r3 = 3.8, 3.9, 3.7
        x_prev1, x_prev2, x_prev3 = 0.5, 0.3, 0.7
        for i in range(self.dim):
            x_prev1 = r1 * x_prev1 * (1 - x_prev1)
            x_prev2 = r2 * x_prev2 * (1 - x_prev2)
            x_prev3 = r3 * x_prev3 * (1 - x_prev3)
            phase_mod = np.sin(x_prev1 * 12 * np.pi) + 0.5 * np.cos(x_prev2 * 8 * np.pi) + 0.3 * np.sin(x_prev3 * 15 * np.pi)
            noise += np.sin(25 * x_normalized[i] + phase_mod) * np.log(1.0 + 0.7 * x_normalized[i]**2)
        
        # Combine all components with adaptive weights
        return (0.25 * fractal + 0.2 * oscillatory + 0.18 * geometric + 
                0.12 * radial + 0.09 * coupling + 0.06 * poly + 0.05 * noise)