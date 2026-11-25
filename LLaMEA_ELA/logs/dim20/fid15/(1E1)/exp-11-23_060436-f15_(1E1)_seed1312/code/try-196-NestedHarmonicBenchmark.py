import numpy as np

class NestedHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component for global attraction
        base = 0.1 * np.sum(x**2)
        
        # Nested harmonic oscillations with varying frequencies and amplitudes
        harmonic = 0
        for i in range(self.dim):
            # Dynamic frequency based on dimension index
            freq = 2.0 + 3.0 * np.sin(0.3 * i)
            
            # Nested harmonic terms with increasing complexity
            term1 = np.sin(freq * x[i]) * np.cos(0.5 * freq * x[i])
            term2 = np.sin(2.0 * freq * x[i]) * np.cos(freq * x[i])
            term3 = np.sin(0.7 * freq * x[i]) * np.cos(1.3 * freq * x[i])
            
            # Dynamic amplitude modulation
            amp_mod = 1.0 + 0.5 * np.sin(0.2 * i) * np.cos(0.1 * i)
            
            harmonic += (term1 + term2 + term3) * amp_mod
        
        # Dynamic conditioning with dimension-dependent scaling
        conditioning = 0
        for i in range(self.dim):
            # Condition number varies across dimensions
            cond_factor = 1.0 + 2.0 * np.sin(0.4 * i) * np.cos(0.3 * i)
            
            # Apply conditioning to each dimension
            conditioning += cond_factor * x[i]**2
        
        # Saddle-point interference patterns with chaotic positioning
        saddle = 0
        for i in range(self.dim):
            # Chaotic saddle point locations
            saddle_loc = 2.5 * np.sin(0.5 * i) * (1.0 + 0.2 * np.cos(0.3 * i))
            
            # Saddle point function with varying curvature
            curvature = 1.0 + 0.8 * np.sin(0.2 * i) * np.cos(0.1 * i)
            saddle += (x[i] - saddle_loc)**2 * (x[i] - saddle_loc)**4 * curvature
        
        # Multi-scale interference with dynamic phase shifts
        interference = 0
        for i in range(self.dim):
            # Multiple interference frequencies with dynamic phase
            freq1 = 1.0 + 0.5 * np.sin(0.3 * i)
            freq2 = 1.5 + 0.3 * np.cos(0.4 * i)
            
            # Phase shift modulation
            phase_shift = 0.2 * np.sin(0.2 * i) * np.cos(0.1 * x[i])
            
            interference += (np.sin(freq1 * x[i] + phase_shift) * 
                           np.cos(freq2 * x[i] + phase_shift) * 
                           np.exp(-0.1 * (x[i] - 1.0)**2))
        
        # Cross-dimensional coupling with dynamic weights
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Dynamic coupling weight based on dimension indices
                weight = 0.5 + 0.5 * np.sin(0.2 * (i + j)) * np.cos(0.1 * i)
                
                # Coupling function with exponential decay
                coupling += weight * np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(x[i] * x[j])
        
        # Asymmetric harmonic component for landscape complexity
        asymmetric = 0
        for i in range(self.dim):
            # Asymmetric modulation based on dimension index
            asym_mod = 1.0 + 0.3 * np.sin(0.4 * i) * np.cos(0.2 * i)
            
            # Asymmetric harmonic terms
            asymmetric += (np.sin(x[i] * asym_mod) * np.exp(-0.1 * x[i]**2) +
                          np.cos(x[i] * asym_mod) * np.exp(-0.15 * x[i]**2))
        
        # Nested chaotic modulation with recursive-like structure
        chaotic = 0
        for i in range(self.dim):
            # Chaotic modulation based on previous dimensions
            if i > 0:
                chaos_mod = 0.2 * np.sin(0.3 * (x[i-1] + x[i])) * np.cos(0.2 * x[i])
                chaotic += chaos_mod
            
            # Add direct chaotic term
            chaotic += 0.15 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Return combined function with optimized weights
        return (base * 0.6 +
                harmonic * 0.7 +
                conditioning * 0.4 +
                saddle * 0.3 +
                interference * 0.5 +
                coupling * 0.3 +
                asymmetric * 0.25 +
                chaotic * 0.4)