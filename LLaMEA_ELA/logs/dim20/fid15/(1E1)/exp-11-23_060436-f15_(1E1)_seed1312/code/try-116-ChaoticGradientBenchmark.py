import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component with enhanced conditioning
        quadratic = np.sum(x**2) * 0.15
        
        # Enhanced chaotic gradient component with multiple attractors and higher frequency modulation
        chaotic_grad = 0
        for i in range(self.dim):
            # Multiple chaotic mappings with different frequencies and amplitudes
            freq1 = 3.0 + 0.6 * np.sin(i * 0.7)
            freq2 = 3.5 + 0.4 * np.cos(i * 0.9)
            freq3 = 2.0 + 0.5 * np.sin(0.6 * i)
            
            # Chaotic terms with varying scales and increased complexity
            term1 = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.4 * x[i]**2)
            term2 = np.cos(freq3 * x[i]) * np.sin(freq1 * x[i]) * np.exp(-0.25 * (x[i] - 1.8)**2)
            term3 = np.sin(freq2 * x[i]) * np.cos(freq3 * x[i]) * np.exp(-0.35 * (x[i] + 1.5)**2)
            
            chaotic_grad += (term1 + term2 + term3) * (1.0 + 0.3 * np.sin(0.4 * i))
        
        # Enhanced saddle point component with variable conditioning and higher density
        saddle = 0
        for i in range(self.dim):
            # Create more dense saddle points at different locations
            saddle_loc = 2.5 * np.sin(i * 0.6)
            condition_factor = 1.0 + 0.7 * np.cos(i * 0.4)
            
            # Saddle point function with varying curvature and higher order terms
            saddle_term = (x[i] - saddle_loc)**2 * (x[i] - saddle_loc)**5 * condition_factor
            saddle += saddle_term
        
        # Multi-scale oscillatory component with increased frequency diversity
        oscillatory = 0
        scales = [0.3, 0.7, 1.2, 2.5, 4.0]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            
            # Multi-frequency oscillation with variable amplitude and phase
            osc_term = np.sin(scale * x[i]) * np.cos(1.8 * scale * x[i]) * np.exp(-0.12 * (x[i] - 2.2)**2)
            osc_term += np.cos(scale * x[i]) * np.sin(2.5 * scale * x[i]) * np.exp(-0.18 * (x[i] + 2.2)**2)
            
            oscillatory += osc_term * (1.0 + 0.2 * np.sin(i * 0.5))
        
        # Cross-dimensional interaction with stronger coupling and dynamic weights
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                weight = 0.7 + 0.3 * np.sin(0.25 * (i + j))  # Increased weight variation
                interaction += weight * np.sin(x[i] * x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
        
        # New component: Variable dimension coupling with dynamic scaling and enhanced nonlinearity
        coupling = 0
        for i in range(self.dim):
            coupling_factor = 1.0 + 0.4 * np.sin(0.5 * i)
            coupling += (np.sin(x[i] * coupling_factor) * np.cos(x[i] * coupling_factor) * 
                        np.exp(-0.25 * x[i]**2) * coupling_factor**2)
        
        # New component: Asymmetric chaotic modulation with increased complexity
        asymmetric = 0
        for i in range(self.dim):
            asym_factor = 1.0 + 0.4 * np.sin(0.35 * i)  # Increased asymmetry
            asym_term = (np.sin(x[i] * asym_factor) * np.exp(-0.12 * x[i]**2) + 
                        np.cos(x[i] * asym_factor) * np.exp(-0.18 * x[i]**2))
            asymmetric += asym_term
        
        # New component: Hybrid polynomial-chaotic with memory and enhanced dynamics
        memory = 0
        for i in range(self.dim):
            memory += (np.sin(x[i]**3) * np.cos(x[i]) * np.exp(-0.15 * (x[i] - 1.2)**2) + 
                      np.cos(x[i]**2) * np.sin(x[i]) * np.exp(-0.2 * (x[i] + 1.2)**2))
        
        # New component: Multi-modal peak clustering with dynamic scaling
        clustering = 0
        for i in range(self.dim):
            cluster_centers = [0.0, 1.5, -1.5, 3.0, -3.0]
            cluster_terms = []
            for center in cluster_centers:
                term = np.exp(-0.2 * (x[i] - center)**2) * np.sin(2.0 * (x[i] - center))
                cluster_terms.append(term)
            clustering += max(cluster_terms)  # Peak clustering effect
        
        # New component: Dynamic conditioning with time-like parameter
        dynamic_cond = 0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.6 * np.sin(0.5 * i + 0.3 * np.sum(x))
            dynamic_cond += (x[i]**2) * cond_factor
        
        # Combine all components with optimized weights
        return (quadratic * 0.9 +
                chaotic_grad * 0.55 +
                saddle * 0.45 +
                oscillatory * 0.65 +
                interaction * 0.42 +  # Increased weight
                coupling * 0.21 +
                asymmetric * 0.32 +   # Increased weight
                memory * 0.24 +
                clustering * 0.18 +   # New component
                dynamic_cond * 0.26)  # New component