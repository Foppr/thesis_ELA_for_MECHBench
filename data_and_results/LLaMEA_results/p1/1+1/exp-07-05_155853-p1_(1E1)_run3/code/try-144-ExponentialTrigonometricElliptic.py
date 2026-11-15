import numpy as np

class ExponentialTrigonometricElliptic:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay components with adaptive rates
        exp_decay = 0
        for i in range(self.dim):
            rate = 0.5 + 0.5 * np.sin(i * 0.6)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.cos(rate * x[i]**2)
        
        # Trigonometric wave interactions with dynamic amplitudes and frequencies
        trig_waves = 0
        for i in range(self.dim):
            amp = 1.0 + 0.3 * np.sin(i * 0.4)
            freq = 1.0 + 0.4 * np.cos(i * 0.5)
            trig_waves += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Adaptive elliptic shaping with dynamic eccentricities
        elliptic = 0
        for i in range(self.dim - 1):
            ecc = 0.3 + 0.7 * np.abs(np.sin(i * 0.3))
            elliptic += (x[i]**2 / (1.0 + ecc)) + (x[i+1]**2 / (1.0 - ecc))
        
        # Dynamic conditioning with chaotic scaling factors
        cond_factor = 0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * 0.7)
            cond_factor += scale * x[i]**2
        
        # Saddle-point distribution with chaotic positioning
        saddle = 0
        for i in range(self.dim):
            pos = -4.0 + 8.0 * (i / max(1, self.dim - 1)) + 0.5 * np.cos(i * 1.2)
            saddle += (x[i] - pos)**2 * (x[i] + pos)**2
        
        # Global interaction term with multiple harmonic components
        global_interaction = 0
        for i in range(self.dim):
            global_interaction += np.sin(0.5 * x[i]) * np.cos(0.3 * x[i]) * np.sin(0.1 * x[i]**2)
        
        # Add noise component for increased ruggedness
        noise = 0.01 * np.sum(np.random.randn(self.dim)**2)
        
        # Combine all components with refined weights
        return 1.5 * exp_decay + 1.2 * trig_waves + 0.8 * elliptic + 0.6 * cond_factor + 0.4 * saddle + 0.3 * global_interaction + noise