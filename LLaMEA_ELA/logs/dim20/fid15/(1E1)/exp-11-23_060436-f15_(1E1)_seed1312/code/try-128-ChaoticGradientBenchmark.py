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
            # Multiple chaotic mappings with different frequencies, amplitudes, and phases
            freq1 = 2.5 + 0.5 * np.sin(i)
            freq2 = 3.0 + 0.3 * np.cos(i)
            freq3 = 1.8 + 0.4 * np.sin(0.5 * i)
            
            # Chaotic terms with varying scales and enhanced nonlinearities
            term1 = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.5 * x[i]**2)
            term2 = np.cos(freq3 * x[i]) * np.sin(freq1 * x[i]) * np.exp(-0.3 * (x[i] - 1.5)**2)
            term3 = np.sin(freq2 * x[i]) * np.cos(freq3 * x[i]) * np.exp(-0.4 * (x[i] + 1.2)**2)
            
            # Add chaotic modulation based on dimension index
            chaotic_mod = 1.0 + 0.2 * np.sin(0.3 * i) + 0.1 * np.cos(0.5 * i)
            chaotic_grad += (term1 + term2 + term3) * chaotic_mod
        
        # Saddle point component with variable conditioning and dynamic curvature
        saddle = 0
        for i in range(self.dim):
            # Create saddle points at different locations with dynamic shifts
            saddle_loc = 2.0 * np.sin(i * 0.5) + 0.5 * np.cos(i * 0.3)
            condition_factor = 1.0 + 0.5 * np.cos(i * 0.3) + 0.2 * np.sin(i * 0.7)
            
            # Enhanced saddle point function with higher-order curvature
            saddle_term = (x[i] - saddle_loc)**2 * (x[i] - saddle_loc)**4 * condition_factor
            saddle += saddle_term
        
        # Multi-scale oscillatory component with increased complexity
        oscillatory = 0
        scales = [0.5, 1.0, 2.0, 3.5, 4.2]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            
            # Multi-frequency oscillation with variable amplitude and phase shifts
            osc_term = np.sin(scale * x[i]) * np.cos(1.5 * scale * x[i]) * np.exp(-0.1 * (x[i] - 2.0)**2)
            osc_term += np.cos(scale * x[i]) * np.sin(2.0 * scale * x[i]) * np.exp(-0.15 * (x[i] + 2.0)**2)
            
            # Add dynamic phase modulation
            phase_mod = 1.0 + 0.1 * np.sin(i * 0.4) + 0.05 * np.cos(i * 0.6)
            oscillatory += osc_term * phase_mod
        
        # Cross-dimensional interaction with enhanced weights and coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                # Dynamic weight based on dimension indices
                weight = 0.6 + 0.2 * np.sin(0.2 * (i + j)) + 0.1 * np.cos(0.3 * i)
                interaction += weight * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Variable dimension coupling with dynamic scaling and enhanced modulation
        coupling = 0
        for i in range(self.dim):
            coupling_factor = 1.0 + 0.3 * np.sin(0.4 * i) + 0.1 * np.cos(0.6 * i)
            coupling += (np.sin(x[i] * coupling_factor) * np.cos(x[i] * coupling_factor) * 
                        np.exp(-0.2 * x[i]**2) * coupling_factor)
        
        # Asymmetric chaotic modulation with enhanced complexity
        asymmetric = 0
        for i in range(self.dim):
            asym_factor = 1.0 + 0.35 * np.sin(0.3 * i) + 0.15 * np.cos(0.4 * i)
            asym_term = (np.sin(x[i] * asym_factor) * np.exp(-0.1 * x[i]**2) + 
                        np.cos(x[i] * asym_factor) * np.exp(-0.15 * x[i]**2))
            asymmetric += asym_term
        
        # Hybrid polynomial-chaotic with memory and enhanced dynamic components
        memory = 0
        for i in range(self.dim):
            # Add higher-order polynomial terms
            memory += (np.sin(x[i]**3) * np.cos(x[i]) * np.exp(-0.1 * (x[i] - 1.0)**2) + 
                      np.cos(x[i]**2) * np.sin(x[i]) * np.exp(-0.15 * (x[i] + 1.0)**2) +
                      x[i]**4 * np.exp(-0.05 * x[i]**2))
        
        # Enhanced multimodal structure with dynamic peaks and complex interactions
        multimodal = 0
        for i in range(self.dim):
            # Dynamic peak locations and heights based on dimension index with additional modulation
            peak_loc = 1.5 * np.sin(0.3 * i) + 0.5 * np.cos(0.4 * i)
            peak_height = 1.0 + 0.4 * np.cos(0.2 * i) + 0.2 * np.sin(0.5 * i)
            
            # Multi-peak chaotic function with varying distances and enhanced complexity
            multimodal += peak_height * (np.sin(x[i] - peak_loc) * np.exp(-0.2 * (x[i] - peak_loc)**2) +
                                       np.cos(x[i] + peak_loc) * np.exp(-0.15 * (x[i] + peak_loc)**2) +
                                       0.3 * np.sin(2 * x[i]) * np.exp(-0.1 * x[i]**2))
        
        # Add a new component: Complex chaotic resonance with dynamic phase locking
        resonance = 0
        for i in range(self.dim):
            freq_mod = 2.0 + 0.5 * np.sin(0.3 * i) + 0.3 * np.cos(0.4 * i)
            resonance += (np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]) * 
                         np.exp(-0.1 * x[i]**2) * (1.0 + 0.1 * np.sin(0.5 * i)))
        
        # Add a new component: Multi-scale fractal-like structure with self-similarity
        fractal = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.2 * np.sin(0.2 * i) + 0.1 * np.cos(0.3 * i)
            fractal += (np.sin(x[i] * scale_factor) * np.cos(x[i] * scale_factor * 0.5) * 
                       np.exp(-0.1 * x[i]**2) * scale_factor)
        
        # Combine all components with adjusted weights for increased complexity
        return (quadratic * 0.8 +
                chaotic_grad * 0.55 +      # Increased weight
                saddle * 0.4 +             # Slightly increased weight
                oscillatory * 0.65 +       # Increased weight
                interaction * 0.42 +       # Increased weight
                coupling * 0.18 +          # Slightly increased weight
                asymmetric * 0.32 +        # Increased weight
                memory * 0.22 +            # Slightly increased weight
                multimodal * 0.35 +        # Increased weight
                resonance * 0.15 +         # New component with moderate weight
                fractal * 0.12)            # New component with low weight