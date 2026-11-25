import numpy as np

class FractalOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Chaotic logistic map based fractal component with varying parameters
        fractal = 0.0
        r_values = [3.55 + 0.1 * np.sin(i * 0.7) for i in range(self.dim)]
        x_prev = np.random.rand()
        for i in range(self.dim):
            x_prev = r_values[i] * x_prev * (1 - x_prev)
            freq = 5.0 + 3.0 * np.sin(i * 0.5)
            amp = 1.5 + 0.5 * np.cos(i * 0.3)
            fractal += amp * np.sin(freq * x_normalized[i] + x_prev) * np.cos(freq * x_normalized[i] + x_prev)
        
        # Multi-scale oscillatory component with frequency modulation
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 15.0 + 10.0 * np.sin(i * 0.8)
            amp = 0.4 + 0.6 * np.cos(i * 0.6)
            phase = 0.3 * np.sin(i * 0.9) + 0.2 * np.cos(i * 0.4)
            oscillatory += amp * np.sin(freq * x_normalized[i] + phase) * np.cos(freq * x_normalized[i] + phase)
        
        # Geometric progression with chaotic weight interactions
        geometric = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                # Chaotic weight modulation using logistic map
                w1 = 0.5 + 0.5 * np.sin(i * 0.3)
                w2 = 0.5 + 0.5 * np.cos(j * 0.4)
                weight = np.exp(-dist * 3.0) * (w1 + w2) / 2.0
                geometric += weight * (x_normalized[i]**2 + x_normalized[j]**2) * np.sin(7 * dist)
        
        # Multi-scale radial basis with chaotic center distribution
        radial = 0.0
        for i in range(self.dim):
            # Chaotic center generation using logistic map
            center = np.sin(i * 0.3) * np.cos(i * 0.4)
            x_center = 0.5 + 0.5 * np.sin(i * 0.2)
            r_center = 3.8 + 0.1 * np.sin(i * 0.7)
            center = r_center * x_center * (1 - x_center)
            width = 0.1 + 0.4 * np.sin(i * 0.5)
            radial += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2)
        
        # Adaptive coupling with chaotic strength modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic strength modulation
                s1 = 0.3 + 0.7 * np.sin(i * 0.4)
                s2 = 0.3 + 0.7 * np.cos(j * 0.3)
                strength = (s1 + s2) / 2.0
                period = 3.0 + 2.0 * np.sin(i * 0.6 + j * 0.5)
                coupling += strength * np.sin(period * (x_normalized[i] - x_normalized[j])) * np.exp(-0.1 * (x_normalized[i] - x_normalized[j])**2)
        
        # Polynomial interaction with chaotic exponents
        poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic exponent modulation
                exp_mod = 1 + 0.5 * np.sin(i * 0.8 + j * 0.7)
                poly += (x_normalized[i] * x_normalized[j])**(2 + exp_mod)
        
        # Logarithmic noise with chaotic phase modulation and variable amplitude
        noise = 0.0
        r = 3.9
        x_prev = 0.5
        for i in range(self.dim):
            x_prev = r * x_prev * (1 - x_prev)
            phase_mod = np.sin(x_prev * 12 * np.pi)
            amp_mod = 0.8 + 0.2 * np.cos(i * 0.6)
            noise += amp_mod * np.sin(25 * x_normalized[i] + phase_mod) * np.log(1.0 + 0.3 * x_normalized[i]**2)
        
        # Combine all components with chaotic weight adjustments
        return (0.25 * fractal + 0.2 * oscillatory + 0.18 * geometric + 
                0.12 * radial + 0.09 * coupling + 0.08 * poly + 0.08 * noise)