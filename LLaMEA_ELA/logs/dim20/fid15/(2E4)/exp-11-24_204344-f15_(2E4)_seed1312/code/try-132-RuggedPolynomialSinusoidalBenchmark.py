import numpy as np

class RuggedPolynomialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Enhanced polynomial potential wells with dynamic exponents and positions
        polynomial = 0.0
        for i in range(self.dim):
            degree = 2 + (i % 4)  # Degrees 2,3,4,5 repeating
            position = 1.0 + 1.5 * np.sin(i * 0.7 + 1.0)
            polynomial += (x[i] - position)**degree
        
        # Chaotic sinusoidal modulations with fractal frequency scaling
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5 + 0.3) * np.cos(i * 0.2)
            amp = 1.0 + 0.8 * np.sin(i * 0.4 + 0.7)
            phase = 0.5 * i + 0.3 * np.sin(i * 0.9)
            sinusoidal += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase * 0.8)
        
        # Cross-dimensional interaction with fractal coupling strengths
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.4 + 0.6 * np.sin(i * j * 0.3 + 0.5)
                cross_terms += coupling * (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j] * 0.5)
        
        # Adaptive noise with chaotic scaling and dynamic correlation
        noise = 0.0
        for i in range(self.dim):
            noise_scale = 0.15 + 0.08 * np.sin(i * 0.7 + 0.4)
            noise += noise_scale * np.random.normal(0, 1) * (1.0 + 0.2 * np.cos(x[i] * 0.6))
        
        # Multi-scale harmonic components with dynamic frequency modulation
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.5 + 1.0 * np.sin(i * 0.3 + 0.2)
            amp = 1.8 + 0.7 * np.cos(i * 0.4 + 0.6)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4)
        
        # Asymmetric exponential terms with dynamic decay and position parameters
        exp_decay = 0.0
        for i in range(self.dim):
            decay_rate = 0.2 + 0.3 * np.sin(i * 0.9 + 0.5)
            offset = 0.3 * np.cos(i * 0.7 + 0.2)
            exp_decay += np.exp(-decay_rate * (x[i] - offset)**2) * np.sin(3 * x[i])
        
        # Fractal-like scaling and combined landscape
        return (0.9 * polynomial + 0.5 * sinusoidal + 0.8 * cross_terms + 
                0.6 * noise + 1.0 * harmonic + 0.3 * exp_decay)