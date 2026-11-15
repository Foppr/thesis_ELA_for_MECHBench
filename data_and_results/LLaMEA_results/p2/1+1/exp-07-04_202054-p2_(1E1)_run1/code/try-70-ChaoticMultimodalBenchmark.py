import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map constants for chaos
        self.r_values = np.random.uniform(3.5, 4.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base spherical term
        f_value = np.sum(x**2)
        
        # Logistic map chaos component
        chaos_sum = 0.0
        for i in range(self.dim):
            # Simple logistic map iteration
            logistic_x = 0.5
            for _ in range(10):
                logistic_x = self.r_values[i] * logistic_x * (1 - logistic_x)
            chaos_sum += logistic_x * np.sin(x[i])
        f_value += 0.5 * chaos_sum
        
        # Fractional polynomial terms with varying exponents
        for i in range(self.dim):
            # Use fractional exponents to create non-smooth behavior
            exponent = 2.5 + 2.0 * np.sin(i)
            f_value += 0.3 * np.abs(x[i])**(exponent) * np.cos(x[i])
            
        # Spherical harmonics-like interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                f_value += 0.2 * np.sin(x[i]) * np.cos(x[j]) * np.sin(x[i] + x[j])
                
        # Multi-scale sinusoidal with chaotic modulation
        for i in range(self.dim):
            freq = 10 * (1 + np.sin(i) * 0.5)
            f_value += 0.4 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.sin(freq * x[i] * 0.3)
            
        # Power-law interaction with chaotic scaling
        for i in range(self.dim):
            power = 1.5 + 0.5 * np.cos(i)
            f_value += 0.25 * np.abs(x[i])**power * np.sin(x[i]**2)
            
        # Cross-variable fractional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractional interaction with chaotic modulation
                mod = 0.5 + 0.5 * np.sin(i + j)
                f_value += 0.15 * np.abs(x[i] * x[j])**(1.2 + mod) * np.cos(x[i] + x[j])
                
        # Multi-modal component with varying amplitudes
        for i in range(self.dim):
            f_value += 0.3 * np.sin(15 * x[i]) * np.cos(12 * x[i]) * np.sin(18 * x[i])
            
        # Add noise to increase irregularity
        noise = np.random.normal(0, 0.05, self.dim)
        f_value += 0.1 * np.sum(noise * x)
        
        # Add a new component: chaotic polynomial with variable exponents
        for i in range(self.dim):
            # Use chaotic sequence for exponents
            exponent = 3.0 + 2.0 * np.sin(i * 0.7)
            f_value += 0.2 * x[i]**exponent * np.cos(x[i])
            
        # Add a new component: multi-scale chaotic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction with variable coupling strength
                coupling = 0.3 + 0.2 * np.sin(i * 0.5 + j * 0.3)
                f_value += coupling * np.sin(x[i] * 1.5) * np.cos(x[j] * 1.2) * np.sin(x[i] * 0.8 + x[j] * 1.1)
                
        # Add a new component: fractional spherical harmonics
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.1 * np.abs(x[i])**1.3 * np.abs(x[j])**1.7 * np.sin(x[i] + x[j])
                
        # Add a new component: chaotic sine-cosine combinations
        f_value += 0.2 * np.sum(np.sin(20 * x) * np.cos(15 * x) * np.sin(25 * x))
        
        # Add a new component: variable fractional powers with chaotic modulation
        for i in range(self.dim):
            # Variable exponent based on chaotic sequence
            exponent = 2.0 + np.sin(i * 0.8) * 1.5
            f_value += 0.25 * np.abs(x[i])**(exponent) * np.sin(x[i] * 0.5)
            
        return f_value