import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2) * 0.1
        
        # Chaotic gradient component with multiple attractors
        chaotic_grad = 0
        for i in range(self.dim):
            # Multiple chaotic mappings with different frequencies and amplitudes
            freq1 = 2.5 + 0.5 * np.sin(i)
            freq2 = 3.0 + 0.3 * np.cos(i)
            freq3 = 1.8 + 0.4 * np.sin(0.5 * i)
            
            # Chaotic terms with varying scales
            term1 = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.5 * x[i]**2)
            term2 = np.cos(freq3 * x[i]) * np.sin(freq1 * x[i]) * np.exp(-0.3 * (x[i] - 1.5)**2)
            term3 = np.sin(freq2 * x[i]) * np.cos(freq3 * x[i]) * np.exp(-0.4 * (x[i] + 1.2)**2)
            
            chaotic_grad += (term1 + term2 + term3) * (1.0 + 0.2 * np.sin(0.3 * i))
        
        # Saddle point component with variable conditioning
        saddle = 0
        for i in range(self.dim):
            # Create saddle points at different locations
            saddle_loc = 2.0 * np.sin(i * 0.5)
            condition_factor = 1.0 + 0.5 * np.cos(i * 0.3)
            
            # Saddle point function with varying curvature
            saddle_term = (x[i] - saddle_loc)**2 * (x[i] - saddle_loc)**4 * condition_factor
            saddle += saddle_term
        
        # Multi-scale oscillatory component
        oscillatory = 0
        scales = [0.5, 1.0, 2.0, 3.5]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            
            # Multi-frequency oscillation with variable amplitude
            osc_term = np.sin(scale * x[i]) * np.cos(1.5 * scale * x[i]) * np.exp(-0.1 * (x[i] - 2.0)**2)
            osc_term += np.cos(scale * x[i]) * np.sin(2.0 * scale * x[i]) * np.exp(-0.15 * (x[i] + 2.0)**2)
            
            oscillatory += osc_term * (1.0 + 0.1 * np.sin(i * 0.4))
        
        # Cross-dimensional interaction with dynamic weights
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited interaction
                weight = 0.6 + 0.2 * np.sin(0.2 * (i + j))  # Slightly increased weight variation
                interaction += weight * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Add a new component: variable dimension coupling with dynamic scaling
        coupling = 0
        for i in range(self.dim):
            coupling_factor = 1.0 + 0.3 * np.sin(0.4 * i)
            coupling += (np.sin(x[i] * coupling_factor) * np.cos(x[i] * coupling_factor) * 
                        np.exp(-0.2 * x[i]**2) * coupling_factor)
        
        # Add a new component: asymmetric chaotic modulation (modified)
        asymmetric = 0
        for i in range(self.dim):
            asym_factor = 1.0 + 0.35 * np.sin(0.3 * i)  # Increased asymmetry
            asym_term = (np.sin(x[i] * asym_factor) * np.exp(-0.1 * x[i]**2) + 
                        np.cos(x[i] * asym_factor) * np.exp(-0.15 * x[i]**2))
            asymmetric += asym_term
        
        # Add a new component: hybrid polynomial-chaotic with memory (modified)
        memory = 0
        for i in range(self.dim):
            memory += (np.sin(x[i]**3) * np.cos(x[i]) * np.exp(-0.1 * (x[i] - 1.0)**2) + 
                      np.cos(x[i]**2) * np.sin(x[i]) * np.exp(-0.15 * (x[i] + 1.0)**2))
        
        # Add a new component: enhanced multimodal structure with dynamic peaks
        multimodal = 0
        for i in range(self.dim):
            # Dynamic peak locations and heights based on dimension index
            peak_loc = 1.5 * np.sin(0.3 * i)
            peak_height = 1.0 + 0.4 * np.cos(0.2 * i)
            
            # Multi-peak chaotic function with varying distances
            multimodal += peak_height * (np.sin(x[i] - peak_loc) * np.exp(-0.2 * (x[i] - peak_loc)**2) +
                                       np.cos(x[i] + peak_loc) * np.exp(-0.15 * (x[i] + peak_loc)**2))
        
        # Combine all components with optimized weights
        return (quadratic * 0.8 +
                chaotic_grad * 0.45 +
                saddle * 0.35 +
                oscillatory * 0.55 +
                interaction * 0.32 +  # Slightly increased weight
                coupling * 0.16 +
                asymmetric * 0.27 +   # Increased weight
                memory * 0.19 +
                multimodal * 0.3)     # New component with moderate weight