import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r = 3.98
        self.logistic_seq = self._generate_logistic_sequence()
        
    def _generate_logistic_sequence(self):
        # Generate a sequence of chaotic values using logistic map
        seq = np.zeros(1000)
        seq[0] = 0.5
        for i in range(1, 1000):
            seq[i] = self.r * seq[i-1] * (1 - seq[i-1])
        return seq[:self.dim] if self.dim < 1000 else seq
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add chaotic scaling factors
        chaotic_factor = 0.0
        for i in range(min(self.dim, len(self.logistic_seq))):
            chaotic_factor += self.logistic_seq[i] * np.sin(x[i])
            
        # Apply adaptive scaling based on chaotic sequence
        result *= (1.0 + 0.5 * chaotic_factor)
        
        # Add spherical harmonic interactions
        for i in range(self.dim):
            # Spherical harmonics with varying degrees
            degree = int((i % 5) + 1)
            result += 0.3 * np.sin(degree * x[i]) * np.cos(degree * x[i])
            
        # Add cross-dimensional coupling with chaotic weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use chaotic sequence for coupling weights
                weight = 0.2 * (1 + self.logistic_seq[i] * self.logistic_seq[j])
                result += weight * np.sin(x[i]**2 + x[j]**2) * np.cos(x[i] * x[j])
                
        # Add nested multimodal structure with fractal-like properties
        for i in range(self.dim):
            # Fractal-like sinusoidal terms with varying frequencies
            freq = 5.0 + 3.0 * np.sin(self.logistic_seq[i])
            result += 0.2 * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
            
        # Add gradient-enhanced polynomial terms
        for i in range(self.dim):
            result += 0.1 * x[i]**4 + 0.05 * x[i]**6
            
        # Add cross-dimensional polynomial interactions with chaotic coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.1 * (1 + self.logistic_seq[i] * self.logistic_seq[j])
                result += coeff * x[i]**3 * x[j]**2
                
        # Add Gaussian perturbations with chaotic positions
        for i in range(self.dim):
            pos = -4.0 + 8.0 * self.logistic_seq[i]
            result += 0.15 * np.exp(-0.5 * ((x[i] - pos) / 0.3)**2)
            
        # Add higher-order terms for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.02 * x[i]**2 * x[j] * x[k]**3
                    
        # Add final chaotic noise term
        noise = 0.01 * np.sum(self.logistic_seq[:self.dim] * np.sin(10 * x))
        result += noise
        
        return result