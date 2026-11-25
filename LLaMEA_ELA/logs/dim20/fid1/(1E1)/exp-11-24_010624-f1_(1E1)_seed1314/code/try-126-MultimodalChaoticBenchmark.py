import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency parameters for sinusoidal components
        self.freq_params = np.array([1.0 + 0.5 * np.sin(i * 0.8) for i in range(dim)])
        # Precompute radial basis centers and widths
        self.rbf_centers = np.random.uniform(-3.0, 3.0, dim)
        self.rbf_widths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add sinusoidal oscillation component with varying frequencies
        for i in range(self.dim):
            result += np.sin(self.freq_params[i] * x[i]) * np.cos(2 * x[i])
            
        # Add radial basis function component
        for i in range(self.dim):
            rbf_val = np.exp(-0.5 * ((x[i] - self.rbf_centers[i]) / self.rbf_widths[i])**2)
            result += 0.3 * rbf_val
            
        # Add cross-dimensional interaction terms with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling = 0.1 * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                result += coupling
                
        # Add polynomial chaos component with mixed exponents
        for i in range(self.dim):
            poly_term = 0.02 * (x[i]**4 + x[i]**3 - 2*x[i]**2 + x[i])
            result += poly_term
            
        # Add a global periodic modulation based on distance from origin
        dist_from_origin = np.sqrt(np.sum(x**2))
        global_mod = np.sin(0.5 * dist_from_origin) * np.cos(0.3 * dist_from_origin)
        result *= (1 + 0.2 * global_mod)
        
        # Add noise component to increase irregularity
        noise = 0.005 * np.sum(np.sin(x * 7))
        result += noise
        
        # Add a modified Schwefel-like term for enhanced multimodality
        schwefel_term = 0.0
        for i in range(self.dim):
            schwefel_term += -x[i] * np.sin(np.sqrt(np.abs(x[i])))
        result += 0.01 * schwefel_term
        
        # Add a periodic component with varying amplitudes and frequencies
        periodic_term = 0.0
        for i in range(self.dim):
            amp = 0.5 + 0.3 * np.sin(i * 0.4)
            freq = 1.5 + 0.8 * np.cos(i * 0.6)
            periodic_term += amp * np.sin(freq * x[i])
        result += 0.02 * periodic_term
        
        return result