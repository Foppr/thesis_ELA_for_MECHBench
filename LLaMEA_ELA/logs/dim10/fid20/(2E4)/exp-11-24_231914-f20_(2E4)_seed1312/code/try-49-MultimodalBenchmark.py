import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term with dynamic weighting
        quadratic = np.sum(x**2) / self.dim
        
        # Enhanced periodic multimodal term with multiple global minima and frequency modulation
        periodic = 0.0
        for i in range(self.dim):
            freq_mod = 1 + 0.5 * np.sin(0.5 * i)
            periodic += (np.sin(freq_mod * 20 * np.pi * x[i]) ** 2 + 
                        0.7 * np.cos(freq_mod * 15 * np.pi * x[i]) ** 2 + 
                        0.3 * np.sin(freq_mod * 25 * np.pi * x[i]) ** 2)
        
        # Add interaction terms between dimensions with varying weights and non-linear coupling
        interaction = 0.0
        for i in range(self.dim - 1):
            interaction += (x[i] - x[i+1])**6 + 0.4 * (x[i] + x[i+1])**4 + 0.2 * np.sin(3 * (x[i] - x[i+1]))
        
        # Add cubic interaction terms with chaotic modulation
        cubic_interaction = 0.0
        for i in range(self.dim - 2):
            chaotic_weight = 0.5 + 0.5 * np.sin(i * 0.7)
            cubic_interaction += (x[i] - x[i+2])**6 + chaotic_weight * (x[i] + x[i+2])**3
        
        # Add quartic interaction terms with variable coupling strength
        quartic_interaction = 0.0
        for i in range(self.dim - 3):
            coupling_strength = 0.1 + 0.3 * np.cos(i * 0.3)
            quartic_interaction += (x[i] - x[i+3])**8 + coupling_strength * (x[i] + x[i+3])**4
        
        # Add chaotic component using modified logistic map with time-varying parameters
        chaotic = 0.0
        r_values = [3.98, 3.88, 3.78, 3.68, 3.58, 3.48, 3.38, 3.28]
        for i in range(self.dim):
            r = r_values[i % len(r_values)] + 0.1 * np.sin(0.2 * i)
            chaotic += np.sin(r * x[i] * (1 - x[i])) ** 2 + 0.2 * np.cos(r * x[i] * (1 - x[i])) ** 2
        
        # Add a dynamic shift based on multi-frequency sine and cosine functions
        shift = 0.0
        for i in range(self.dim):
            shift += 0.6 * np.sin(5 * x[i]) + 0.4 * np.cos(7 * x[i]) + 0.2 * np.sin(3 * x[i]) + 0.1 * np.cos(9 * x[i])
        
        # Add higher-order polynomial interactions with variable exponents
        high_order = 0.0
        for i in range(self.dim - 4):
            exponent = 8 + 2 * np.sin(i * 0.5)
            high_order += (x[i] - x[i+4])**exponent + 0.15 * (x[i] + x[i+4])**5
        
        # Add exponential and logarithmic terms with complex phase modulation
        exp_term = 0.0
        log_term = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.sin(0.3 * i)
            exp_term += np.exp(-0.5 * x[i]**2) * np.sin(10 * x[i] + phase)
            log_term += np.log(np.abs(x[i]) + 1) * np.cos(5 * x[i] + phase)
        
        # Add hyperbolic and trigonometric mixed terms for increased complexity
        hyperbolic = 0.0
        trig_mixed = 0.0
        for i in range(self.dim):
            hyperbolic += np.sinh(0.1 * x[i]) ** 2 + 0.3 * np.cosh(0.15 * x[i]) ** 2
            trig_mixed += np.tan(np.pi * x[i] / 10) ** 2 + 0.2 * np.sec(np.pi * x[i] / 8) ** 2
        
        # Combine all terms to create challenging landscape with increased complexity
        return (quadratic + 
                0.5 * periodic + 
                0.25 * interaction + 
                0.15 * cubic_interaction + 
                0.08 * quartic_interaction + 
                0.3 * chaotic + 
                0.3 * shift + 
                0.1 * high_order + 
                0.1 * exp_term + 
                0.05 * log_term + 
                0.03 * hyperbolic + 
                0.02 * trig_mixed)