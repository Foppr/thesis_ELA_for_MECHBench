import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2) * 0.1
        
        # Chaotic gradient component with multiple attractors and enhanced nonlinearity
        chaotic_grad = 0
        for i in range(self.dim):
            # Multiple chaotic mappings with different frequencies and amplitudes
            freq1 = 3.0 + 0.7 * np.sin(i * 0.5)
            freq2 = 3.5 + 0.4 * np.cos(i * 0.3)
            freq3 = 2.0 + 0.6 * np.sin(0.7 * i)
            
            # Chaotic terms with varying scales and higher-order nonlinearities
            term1 = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.5 * x[i]**2)
            term2 = np.cos(freq3 * x[i]) * np.sin(freq1 * x[i]) * np.exp(-0.3 * (x[i] - 1.5)**2)
            term3 = np.sin(freq2 * x[i]) * np.cos(freq3 * x[i]) * np.exp(-0.4 * (x[i] + 1.2)**2)
            
            chaotic_grad += (term1 + term2 + term3) * (1.0 + 0.3 * np.sin(0.4 * i))
        
        # Saddle point component with variable conditioning and enhanced complexity
        saddle = 0
        for i in range(self.dim):
            # Create saddle points at different locations with dynamic shifts
            saddle_loc = 2.5 * np.sin(i * 0.6) + 0.5 * np.cos(i * 0.4)
            condition_factor = 1.0 + 0.7 * np.cos(i * 0.5)
            
            # Saddle point function with higher-order curvature
            saddle_term = (x[i] - saddle_loc)**2 * (x[i] - saddle_loc)**5 * condition_factor
            saddle += saddle_term
        
        # Multi-scale oscillatory component with memory effects and enhanced modulation
        oscillatory = 0
        scales = [0.7, 1.3, 2.2, 3.8, 4.5]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            
            # Multi-frequency oscillation with variable amplitude and memory
            osc_term = np.sin(scale * x[i]) * np.cos(1.8 * scale * x[i]) * np.exp(-0.1 * (x[i] - 2.0)**2)
            osc_term += np.cos(scale * x[i]) * np.sin(2.5 * scale * x[i]) * np.exp(-0.15 * (x[i] + 2.0)**2)
            
            # Add memory effect
            if i > 0:
                osc_term += 0.2 * np.sin(x[i-1] * scale) * np.cos(x[i] * scale)
            
            oscillatory += osc_term * (1.0 + 0.2 * np.sin(i * 0.5))
        
        # Cross-dimensional interaction with dynamic weights and memory
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                weight = 0.7 + 0.3 * np.sin(0.25 * (i + j))  # Increased weight variation
                interaction += weight * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
                # Add memory-dependent interaction
                if i > 0 and j > 0:
                    interaction += 0.1 * np.sin(x[i-1] * x[j-1]) * np.exp(-0.05 * (x[i-1]**2 + x[j-1]**2))
        
        # Add a new component: variable dimension coupling with dynamic scaling and feedback
        coupling = 0
        for i in range(self.dim):
            coupling_factor = 1.0 + 0.4 * np.sin(0.5 * i)
            coupling += (np.sin(x[i] * coupling_factor) * np.cos(x[i] * coupling_factor) * 
                        np.exp(-0.2 * x[i]**2) * coupling_factor +
                        0.1 * np.sin(x[i] * coupling_factor**2) * np.cos(x[i] * coupling_factor**2))
        
        # Add a new component: asymmetric chaotic modulation with feedback
        asymmetric = 0
        for i in range(self.dim):
            asym_factor = 1.0 + 0.4 * np.sin(0.35 * i)
            asym_term = (np.sin(x[i] * asym_factor) * np.exp(-0.1 * x[i]**2) + 
                        np.cos(x[i] * asym_factor) * np.exp(-0.15 * x[i]**2))
            
            # Add feedback term
            if i > 0:
                asym_term += 0.05 * (np.sin(x[i-1] * asym_factor) * np.exp(-0.05 * x[i-1]**2))
            
            asymmetric += asym_term
        
        # Add a new component: hybrid polynomial-chaotic with memory and dynamic exponents
        memory = 0
        for i in range(self.dim):
            # Dynamic exponent based on dimension index
            exp_factor = 1.5 + 0.5 * np.sin(i * 0.3)
            memory += (np.sin(x[i]**exp_factor) * np.cos(x[i]) * np.exp(-0.1 * (x[i] - 1.0)**2) + 
                      np.cos(x[i]**(exp_factor*0.8)) * np.sin(x[i]) * np.exp(-0.15 * (x[i] + 1.0)**2))
        
        # Add a new component: multi-scale chaotic resonance with time-dependent modulation
        resonance = 0
        for i in range(self.dim):
            # Time-dependent frequency modulation
            freq_mod = 1.0 + 0.3 * np.sin(0.5 * i + 0.2 * np.sum(x[:i]) if i > 0 else 0)
            resonance += (np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]) * 
                         np.exp(-0.1 * x[i]**2) * freq_mod +
                         0.15 * np.sin(2 * freq_mod * x[i]) * np.cos(2 * freq_mod * x[i]))
        
        # Combine all components with optimized weights
        return (quadratic * 0.7 +
                chaotic_grad * 0.5 +
                saddle * 0.4 +
                oscillatory * 0.6 +
                interaction * 0.35 +  # Increased weight
                coupling * 0.2 +
                asymmetric * 0.3 +   # Increased weight
                memory * 0.2 +
                resonance * 0.25)